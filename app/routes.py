from app import app
from flask import render_template, request
import requests

@app.route('/')
def index():

    # must create a base template with no jinja otherwise there will be errors as jinja will attempt to compute things that dont exist

    return render_template('home.html',)

@app.route('/status')
def status_query():
    
    lines_request = requests.get('https://api.tfl.gov.uk/Line/Mode/tube?app_id=4216733b&app_key=1a60dd098dc91fca5006de8b92b72cee').json()

    lines = []
    for i in range(len(lines_request)):
        lines.append(lines_request[i]['id'])

    line = request.args.get('line')

    data = requests.get(f'https://api.tfl.gov.uk/Line/{line}/Status?app_id=4216733b&app_key=1a60dd098dc91fca5006de8b92b72cee')

    return render_template('home.html', lines=lines, len=len(lines), data = data.text)