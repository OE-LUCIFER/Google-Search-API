# Google-Search-API 



## Table of Contents



- [Google-Search-API](#google-search-api)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Project Structure](#project-structure)
  - [Technologies](#technologies)
  - [Setup and Installation](#setup-and-installation)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
    - [In replit just clone this repl](#in-replit-just-clone-this-repl)
    - [Heroku Quick Deploy](#heroku-quick-deploy)
  - [License](#license)



## Introduction



Google-Search-API is a Python-based project designed for interacting with the Google Search to retrieve search results efficiently.



## Project Structure



The project structure includes the following directories:



- **Root**: Contains configuration files such as .gitignore, Dockerfile, and requirements.txt.

- **apis**: Functionality related to API interactions.

- **documents**: Handles document-related tasks like extracting query results and webpage content.

- **networks**: Deals with network-related functionalities including fetching webpages and managing network configurations.

- **utils**: Contains utility functions such as environment variable handling and logging.



## Technologies



Google-Search-API utilizes the following technologies:



- **Languages**: Python

- **Frameworks/Libraries**: Beautiful Soup, FastAPI, Pydantic, Requests, and more (detailed in requirements.txt).



## Setup and Installation



### Prerequisites



- Python 3.11 or higher

- Docker (optional, for containerization)



### Installation Steps



1. **Clone the Repository:**



```

git clone https://github.com/OE-LUCIFER/Google-Search-API.git

```



2. **Install Dependencies:**



```

pip install -r requirements.txt

```


3.How to run server?

```

cd apis

```

```

python search_api.py

```
### In replit just clone this repl

[![Run on Replit](https://replit.com/badge/github/OE-LUCIFER/Google-Search-API)](https://replit.com/@helpingai/Google-Search-API?v=1)

### [Heroku Quick Deploy](https://heroku.com/about)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/OE-LUCIFER/Google-Search-API)

Provides:
- Easy Deployment of App
- A HTTPS url (https://\<your app name\>.herokuapp.com)

Notes:
- Requires a **PAID** Heroku Account.
- Sometimes has issues with auto-redirecting to `https`. Make sure to navigate to the `https` version of your app before adding as a default search engine.

```python
# Thanks to Himanshu Aggarwal for This python code
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from documents.webpage_content_extractor import BatchWebpageContentExtractor
from networks.webpage_fetcher import BatchWebpageFetcher
from documents.query_results_extractor import QueryResultsExtractor
from networks.google_searcher import GoogleSearcher

def finalextractor():
    print('---------------Here Running for GoogleSearch--------------------')
    google_searcher = GoogleSearcher()
    query_results_extractor = QueryResultsExtractor()
    query_html_path = google_searcher.search(
                    query='mango',
                    result_num=10,
                    safe=False,
                    overwrite=False,
                )
    query_search_results = query_results_extractor.extract(query_html_path)
    urls = []
    for query_extracts in query_search_results['query_results']:
        urls.append(query_extracts['url'])  # Ensure this key exists to avoid KeyError
    print('---------------Batch Webpage Fetcher--------------------')
    batch_webpage_fetcher = BatchWebpageFetcher()
    url_and_html_path_list = batch_webpage_fetcher.fetch(
                    urls,
                    overwrite=False,
                    output_parent=query_search_results["query"],
                )
    print('---------------Batch Webpage Extractor--------------------')
    batch_webpage_content_extractor = BatchWebpageContentExtractor()
    webpageurls = [url_and_html['html_path'] for url_and_html in url_and_html_path_list]
    html_path_and_extracted_content_list = (
                    batch_webpage_content_extractor.extract(webpageurls)
                )
    for html_path_and_extracted_content in html_path_and_extracted_content_list: 
        print(html_path_and_extracted_content['extracted_content'])

finalextractor()
```
## License

This project is licensed under the HelpingAI Simplified Universal License. For the full license text, please check the [LICENSE.md](https://raw.githubusercontent.com/OE-LUCIFER/Google-Search-API/main/LICENSE.md) file in the project repository.
