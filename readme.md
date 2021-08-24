# RESTful API for Covid cases by state
Uses [covidactnow.org's](https://covidactnow.org/data-api) API to get Covid numbers and cases by state
## sample flow
GET request:
```json
{
  "MI": {
    "cases": 1039017, 
    "deaths": 21384, 
    "lastUpdatedDate": "2021-08-23", 
    "population": 9986857, 
    "state": "MI"
  }
}
```
POST request: `{ some_data_you_posted }` >> `database.txt`  
Check out Covid data JSON: `your_local_host/v1/coviddata/`
## to run local server
```
$ pip install -r requirements.txt
$ py run.py
```
NOTE: The covid_data API has a direct dependency on covidactnow's API, which requires an API key. Make sure to set env variables properly.
## todo
- [ ] improve functionality of API
- [ ] build ui (link client repo here...)
## helpful links
- https://www.geeksforgeeks.org/get-post-requests-using-python/
- https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
- https://stackoverflow.com/questions/52897200/getting-flask-request-data
- https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
- https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line
