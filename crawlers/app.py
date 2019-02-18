#!flask/bin/python
import subprocess
from flask import Flask, jsonify
from crawlers.spiders.rozetka import RozetkaSpider

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World"

@app.route('/api/scrape/<int:scraper_id>', methods=['GET'])
def scrape(scraper_id):
    if scraper_id == 1:
        command = ['scrapy', 'crawl', 'rozetka']
        subprocess.Popen(command)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
