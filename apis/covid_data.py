from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from dotenv import load_dotenv
from decouple import config


load_dotenv()
DATABASE_CONN = "db/database.txt"

class CovidData(Resource):
    def get(self):
        return jsonify(covidactnow_api_ingest())
    
    def post(self):
        import datetime

        data = request.get_json() 
        raw =  request.get_data()

        # write data to database
        ct = datetime.datetime.now()
        db = open(DATABASE_CONN, "a")
        decoded_raws = raw.decode("utf-8")
        decoded_list = decoded_raws.split("&")
        db.write(str({str(ct): decoded_list})+'\n')
        db.close()

        return make_response(jsonify({'data': data}), 200)

'''
Utility function ingests json from Covid Act Now API [https://covidactnow.org/data-api]
and satisfies req 1 (refer to readme)

Returns
-------
dict
    data of covid related cases by state
'''
def covidactnow_api_ingest():
    import requests
    API_KEY = config('API_KEY')
    print('running server with API_KEY =', API_KEY)
    URL = 'https://api.covidactnow.org/v2/states.json?apiKey=' + str(API_KEY)
    r = requests.get(url = URL)
    data = r.json()

    def ingest():
        out = {}
        for item in data:
            out[item['state']] = {
                'state': item['state'],
                'population': item['population'],
                'cases': item['actuals']['cases'],
                'deaths': item['actuals']['deaths'],
                'lastUpdatedDate': item['lastUpdatedDate']
            }
        return out

    return ingest()