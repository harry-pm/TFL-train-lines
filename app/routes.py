from app import app
from flask import render_template, request
import requests

@app.route('/')
def index():

    lines_request = requests.get('https://api.tfl.gov.uk/Line/Mode/tube').json()

    for i in range(len(lines_request)):
        lines = lines_request[i]['id']

    print(lines)

    return render_template('home.html')

@app.route('/status')
def status_query():

    line = request.args.get('line')

    data = requests.get(f'https://api.tfl.gov.uk/Line/{line}/Status')

    return render_template('home.html', data = data.text)