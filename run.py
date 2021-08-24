'''
api https://covidactnow.org/data-api
Current data for all states, counties, or metros
https://api.covidactnow.org/v2/states.json?apiKey=YOUR_KEY_HERE
https://api.covidactnow.org/v2/counties.json?apiKey=YOUR_KEY_HERE
https://api.covidactnow.org/v2/cbsas.json?apiKey=YOUR_KEY_HERE
'''

from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from apis.covid_data import CovidData

app = Flask(__name__)
api = Api(app)

api.add_resource(CovidData, '/v1/coviddata/')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)