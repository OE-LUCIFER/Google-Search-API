import argparse
import os
import sys
import uvicorn
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Union
from sse_starlette.sse import EventSourceResponse, ServerSentEvent
from utils.logger import logger
from networks.google_searcher import GoogleSearcher
from networks.webpage_fetcher import BatchWebpageFetcher
from documents.query_results_extractor import QueryResultsExtractor
from documents.webpage_content_extractor import BatchWebpageContentExtractor
from utils.logger import logger


class SearchAPIApp:
    def __init__(self):
        self.app = FastAPI(
            docs_url="/",
            title="Web Search API",
            swagger_ui_parameters={"defaultModelsExpandDepth": -1},
            version="1.0",
        )
        self.setup_routes()

    class QueriesToSearchResultsPostItem(BaseModel):
        queries: list = Field(
            default=[""],
            description="(list[str]) Queries to search",
        )
        result_num: int = Field(
            default=10,
            description="(int) Number of search results",
        )
        safe: bool = Field(
            default=False,
            description="(bool) Enable SafeSearch",
        )
        types: list = Field(
            default=["web"],
            description="(list[str]) Types of search results: `web`, `image`, `videos`, `news`",
        )
        extract_webpage: bool = Field(
            default=False,
            description="(bool) Enable extracting main text contents from webpage, will add `text` filed in each `query_result` dict",
        )
        overwrite_query_html: bool = Field(
            default=False,
            description="(bool) Overwrite HTML file of query results",
        )
        overwrite_webpage_html: bool = Field(
            default=False,
            description="(bool) Overwrite HTML files of webpages from query results",
        )

    def queries_to_search_results(self, item: QueriesToSearchResultsPostItem):
        google_searcher = GoogleSearcher()
        queries_search_results = []
        for query in item.queries:
            query_results_extractor = QueryResultsExtractor()
            if not query.strip():
                continue
            query_html_path = google_searcher.search(
                query=query,
                result_num=item.result_num,
                safe=item.safe,
                overwrite=item.overwrite_query_html,
            )
            query_search_results = query_results_extractor.extract(query_html_path)
            queries_search_results.append(query_search_results)
        logger.note(queries_search_results)

        if item.extract_webpage:
            queries_search_results = self.extract_webpages(
                queries_search_results,
                overwrite_webpage_html=item.overwrite_webpage_html,
            )
        return queries_search_results

    def extract_webpages(self, queries_search_results, overwrite_webpage_html=False):
        for query_idx, query_search_results in enumerate(queries_search_results):
            # Fetch webpages with urls
            batch_webpage_fetcher = BatchWebpageFetcher()
            urls = [
                query_result["url"]
                for query_result in query_search_results["query_results"]
            ]
            url_and_html_path_list = batch_webpage_fetcher.fetch(
                urls,
                overwrite=overwrite_webpage_html,
                output_parent=query_search_results["query"],
            )

            # Extract webpage contents from htmls
            html_paths = [
                str(url_and_html_path["html_path"])
                for url_and_html_path in url_and_html_path_list
            ]
            batch_webpage_content_extractor = BatchWebpageContentExtractor()
            html_path_and_extracted_content_list = (
                batch_webpage_content_extractor.extract(html_paths)
            )

            # Build the map of url to extracted_content
            html_path_to_url_dict = {
                str(url_and_html_path["html_path"]): url_and_html_path["url"]
                for url_and_html_path in url_and_html_path_list
            }
            url_to_extracted_content_dict = {
                html_path_to_url_dict[
                    html_path_and_extracted_content["html_path"]
                ]: html_path_and_extracted_content["extracted_content"]
                for html_path_and_extracted_content in html_path_and_extracted_content_list
            }

            # Write extracted contents (as 'text' field) to query_search_results
            for query_result_idx, query_result in enumerate(
                query_search_results["query_results"]
            ):
                url = query_result["url"]
                extracted_content = url_to_extracted_content_dict[url]
                queries_search_results[query_idx]["query_results"][query_result_idx][
                    "text"
                ] = extracted_content

        return queries_search_results

    def setup_routes(self):
        self.app.post(
            "/queries_to_search_results",
            summary="Search queries, and extract contents from results",
        )(self.queries_to_search_results)


class ArgParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(ArgParser, self).__init__(*args, **kwargs)

        self.add_argument(
            "-s",
            "--server",
            type=str,
            default="0.0.0.0",
            help="Server IP for Web Search API",
        )
        self.add_argument(
            "-p",
            "--port",
            type=int,
            default=21111,
            help="Server Port for Web Search API",
        )

        self.add_argument(
            "-d",
            "--dev",
            default=False,
            action="store_true",
            help="Run in dev mode",
        )

        self.args = self.parse_args(sys.argv[1:])


app = SearchAPIApp().app

if __name__ == "__main__":
    args = ArgParser().args
    if args.dev:
        uvicorn.run("__main__:app", host=args.server, port=args.port, reload=True)
    else:
        uvicorn.run("__main__:app", host=args.server, port=args.port, reload=False)

    # python -m apis.search_api      # [Docker] in product mode
    # python -m apis.search_api -d   # [Dev]    in develop mode
