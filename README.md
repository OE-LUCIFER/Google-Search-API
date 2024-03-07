# Google-Search-API 



## Table of Contents



1. [Introduction](#introduction)

2. [Project Structure](#project-structure)

3. [Technologies](#technologies)

4. [Setup and Installation](#setup-and-installation)

5. [License](#license)



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


## License



This project is licensed under the HelpingAI Simplified Universal License. For the full license text, please check the [LICENSE.md](https://raw.githubusercontent.com/OE-LUCIFER/Google-Search-API/main/LICENSE.md) file in the project repository.
