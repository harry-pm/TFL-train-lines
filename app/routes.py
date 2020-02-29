from app import app
from flask import render_template
import requests

@app.route('/')
def index():

    data = requests.get('https://api.tfl.gov.uk/Line/northern')

    print(data.text)

    return render_template('home.html', data = data.text)