# Product catalog crawler
## Description
Hi folks, this repo will contain all the necessary data for our workshop **Recurrent web crawling with [Scrapy](https://scrapy.org/).**
We will try to scrape products information from several websites and store them to local files. Afterward, we will create a recurrent scheduling mechanism so these scrapers will be started automatically on a daily basis and files with data will be updated.
I can change the dependency tree until 16/02/2019, so it recommended to follow installation instructions after that date.

TODO: Create a simple web server to represent the crawled data?

## Prerequisites
You should have [python version > 3.5](https://www.python.org/downloads/) installed on your OS. We will be working with command line so it would be good to have at least basic knowledge how to use it on your OS *(cd into the directory, delete the directory, show the current path, etc)*
### Installation instructions
1. Clone this repository, cd into it;
2. Install [pipenv](https://github.com/pypa/pipenv) to use separate virtual environment: `pip install pipenv` .
3. Install dependencies from the Pipfile: `pipenv install` (Note that if you have python 2 installed on your system you should specify python 3 version directly: `pipenv --python 3 install` )
4. Activate the virtualenv: `pipenv shell` - if you received no error's - you did everything correctly! Otherwise, try to figure out what went wrong
