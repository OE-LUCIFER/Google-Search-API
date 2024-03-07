# Google-Search-API 

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Technologies](#technologies)
4. [Setup and Installation](#setup-and-installation)
5. [License](#license)

## Introduction

Google-Search-API is a Python-based project designed for interacting with the Google Search API to retrieve search results efficiently.

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

3. **(Optional) Docker Setup:**

- **Build the Docker image:**

```
docker build -t google-search-api .
```

- **Run the Docker container:**

```
docker run -p 21111:21111 google-search-api
```

## License

This project is licensed under the HelpingAI Simplified Universal License. For the full license text, please check the [LICENSE.md](https://raw.githubusercontent.com/OE-LUCIFER/Google-Search-API/main/LICENSE.md) file in the project repository.
