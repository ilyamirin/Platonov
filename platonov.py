from flask import Flask, render_template, url_for
from os import listdir, path

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/pictures_urls")
def pictures_urls():
    result = {'pictures': list()}
    for pict in listdir(path.join('static','pictures')):
        result['pictures'].append(url_for('static', filename='pictures/'+pict))
    return result

