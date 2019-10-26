from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug import secure_filename

#app = Flask(__name__)
bp = Blueprint('main', __name__)

@bp.route("/")
def main():
    #a = get database info
    return render_template('template/index.html')

'''
if __name__ == '__main__':
    app.run(debug=True)

@bp.route("")
def index():
'''
