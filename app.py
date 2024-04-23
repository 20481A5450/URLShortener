from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

@app.route('/urlshortner')
def urlshortner():
    return render_template('urlshortner.html')

if __name__ == '__main__':
    app.run(debug=True)
