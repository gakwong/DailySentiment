from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import webscrape_script as wbscr
import image_script as imgscr
import nlanguage_script as langscr
import requests
#import urlib2

app = Flask(__name__, instance_relative_config=True, static_folder='static', static_url_path='/static')
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        newsub = request.form['subreddit']
        #print(newsub)
        data = runWebscrape(newsub)
        title = get_title(data, 0)
        url = get_link(data, 0)
        sentiment = np.round(get_sentiment(data),5)
        sub_link = "https://www.reddit.com/r/" + newsub
        exists = check_url(sub_link)
        if not exists:
            sub_link =  "https://www.reddit.com/r/worldnews/"
        return render_template("index.html", headline = title, link = url, sentiment = sentiment, subreddit = newsub, sub_link= sub_link, exists= exists)
    else:
        #a = get database info
        data = runWebscrape("WorldNews")
        #print(data.to_string())
        title = get_title(data, 0)
        url = get_link(data, 0)
        sentiment = np.round(get_sentiment(data), 5)
        #hlOneImg = data.iloc[0]['title']
        #hlTwoImg = data.iloc[1]['title']
        #imgscr.main(hlOneImg);
        #imgscr.main(hlTwoImg);
        return render_template('index.html', headline = title, link = url, sentiment = sentiment, subreddit="WorldNews", sub_link = "https://www.reddit.com/r/worldnews/", exists=True)


@app.route("/method")
def method():
    return render_template('method.html')

def runWebscrape( subreddit ):
    dict = wbscr.main(subreddit)
    return dict

def runLangScript( phrase ):
    return langscr.main( phrase )

def get_sentiment( data ):
    lst = [runLangScript(get_title(data, index)) for index in range(8)]
    return np.average(lst)

def get_title(data, index):
    new_data = data['title']
    title = str(new_data[index])
    return title

def get_link(data, index):
    new_data = data['url']
    url = str(new_data[index])
    return url

def check_url(link):
    request = requests.get(link)
    if request.status_code == 200:
        return True
    else:
        return False



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
