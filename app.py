from flask import Flask, render_template,redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from utils import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_timestamp = db.Column(db.DateTime, nullable=False)
    original_url = db.Column(db.String(200), nullable=False)
    short_url = db.Column(db.String(50), nullable=False)


@app.route('/')
def index():
    return render_template('landing_page.html')


@app.route('/urlshortner', methods=["GET", "POST"])
def url_shortner():
    if request.method == "POST":
        short_name = request.form.get('name')
        url = request.form.get('url')

        if 'http' not in url:
            url = f'http://{url}'
        
        if valid_url(url):
            if name_available(short_name) is None:
                add_url(short_name, url)
                return render_template("urlshortner.html", short_name=short_name)
            else:
                return render_template('urlshortner.html', msg='Short name not available')
    else:
        return render_template('urlshortner.html', msg='Invalid url')

    return render_template('urlshortner.html')


@app.route('/<path:short_name>')
def redirect_url(short_name):
    url = get_url(short_name)
    if url is None:
        return "<h2 style='color:red'> Invalid URL </h2>"
    return redirect(url.url)

if __name__ == '__main__':
    app.run(debug=True)
