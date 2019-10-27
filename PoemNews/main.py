from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from . import webscrape_script as wbscr
from . import image_script as imgscr
from . import nlanguage_script as langscr
#from . import tts_script as ttsscr

#app = Flask(__name__)
bp = Blueprint('main', __name__)

@bp.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        newsub = request.form['subreddit']
        #print(newsub)
        data = runWebscrape(newsub)
        print(data.to_string())
        title = get_title(data, 0)
        url = get_link(data, 0)
        sentiment = np.round(get_sentiment(data),5)
        return render_template("index.html", headline = title, link = url, sentiment = sentiment, srname = newsub)
    else:
        #a = get database info
        data = runWebscrape("WorldNews")
        print(data.to_string())
        title = get_title(data, 0)
        url = get_link(data, 0)
        sentiment = np.round(get_sentiment(data), 5)
        #hlOneImg = data.iloc[0]['title']
        #hlTwoImg = data.iloc[1]['title']
        #imgscr.main(hlOneImg);
        #imgscr.main(hlTwoImg);
        return render_template('index.html', headline = title, link = url, sentiment = sentiment, srname = "WorldNews")

@bp.route("/method")
def method():
    return render_template('method.html')

def runWebscrape( subreddit ):
    dict = wbscr.main(subreddit)
    return dict
    #print(dict.to_string())

def runLangScript( phrase ):
    return langscr.main( phrase )

#def runTTSScript( phrase ):
#    ttsscr.main( phrase )

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

'''
if __name__ == '__main__':
    app.run(debug=True)

@bp.route("")
def index():
'''
