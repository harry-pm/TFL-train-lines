from app import app
from flask import render_template, request
import requests

lines_request = requests.get('https://api.tfl.gov.uk/Line/Mode/tube?app_id=4216733b&app_key=1a60dd098dc91fca5006de8b92b72cee').json()

lines = []
for i in range(len(lines_request)):
    lines.append(lines_request[i]['id'])

@app.route('/')
def index():

    return render_template('home.html', lines = lines)


@app.route('/status')
def status_query():
    
    line = request.args.get('line')

    data = requests.get(f'https://api.tfl.gov.uk/Line/{line}/Status?app_id=4216733b&app_key=1a60dd098dc91fca5006de8b92b72cee')

    return render_template('home.html',  data = data.text, lines = lines)