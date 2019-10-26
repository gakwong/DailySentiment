from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename
import pandas as pd
from . import webscrape_script as wbscr
from . import image_script as imgscr

#app = Flask(__name__)
bp = Blueprint('main', __name__)

@bp.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        newsub = request.form['subreddit']
        print(newsub)
        data = runWebscrape(newsub)
        print(data.to_string())
        new_data = convert_string(data, 0)
        return render_template("index.html", data = new_data)
    else:
        #a = get database info
        data = runWebscrape("WorldNews")
        print(data.to_string())
        new_data = convert_string(data, 0)
        #hlOneImg = data.iloc[0]['title']
        #hlTwoImg = data.iloc[1]['title']
        #imgscr.main(hlOneImg);
        #imgscr.main(hlTwoImg);
        return render_template('index.html', data = new_data)

def runWebscrape( subreddit ):
    dict = wbscr.main(subreddit)
    return dict
    #print(dict.to_string())

def convert_string(data, index):
    new_data = data['title']
    s1 = str(new_data[index])
    return s1

'''
if __name__ == '__main__':
    app.run(debug=True)

@bp.route("")
def index():
'''
