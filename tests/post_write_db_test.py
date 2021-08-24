import requests
import sys

def test():
    API_ENDPOINT = 'http://127.0.0.1:5000/v1/coviddata/'
    try:
        data = {
            'api_state': str(sys.argv[1]),
            'api_cases': str(sys.argv[2]),
        }
    except IndexError:
        print('test exited with return=1')
        return 1
    r = requests.post(url = API_ENDPOINT, data = data)
    print('test exited with return=0')
    return 0

if __name__ == "__main__":
    test()