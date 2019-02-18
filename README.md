# Product catalog crawler
## Description
Hi folks, this repo will contain all the necessary data for our workshop **Recurrent web crawling with [Scrapy](https://scrapy.org/).**
We will try to scrape products information from several websites and store them to local files. Afterward, we will create a recurrent scheduling mechanism so these scrapers will be started automatically on a daily basis and files with data will be updated.
I can change the dependency tree until 16/02/2019, so it recommended to follow installation instructions after that date.


## Prerequisites
You should have [python version > 3.5](https://www.python.org/downloads/) installed on your OS. We will be working with command line so it would be good to have at least basic knowledge how to use it on your OS *(cd into the directory, delete the directory, show the current path, etc)* . Unix OS is preferred, if you're on the Windows it is required you to install Ubuntu on the Virtualbox.
### Detailed steps, used during the workshop:
1. Clone this repository, cd into it;
2. Install [pipenv](https://github.com/pypa/pipenv) to use separate virtual environment: `pip install pipenv` .
3. Install dependencies from the Pipfile: `pipenv install` (Note that if you have python 2 installed on your system you should specify python 3 version directly: `pipenv --python 3 install` )
4. Activate the virtualenv: `pipenv shell` - if you received no error's - you did everything correctly! Otherwise, try to figure out what went wrong
5. Start new scrapy project from the root project directory: `scrapy startproject crawlers`; cd crawlers
6. `scrapy genspider rozetka rozetka.com.ua`
7. Modify files settings.py, rozetka.py, items.py
8. Check if crawling is working: `scrapy crawl rozetka`
9. Add `app.py` to the directory where `scrapy.cfg` exists
10. Start the Flask app: `python app.py`
11. Open in the browser `localhost:5000/api/scrape/1`
12. Check scraping works in the logs


Presentation can be found [here](https://docs.google.com/presentation/d/145ceXdZAfO_VgA7VZG95RZkyEfEFdS_eVLawtRk0IK4/edit?usp=sharing)
Code paste [here](http://collabedit.com/dfanr)
