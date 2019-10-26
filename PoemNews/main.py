from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
#app = Flask(__name__)
bp = Blueprint('Poem', __name__)

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
