import requests
import sys

def test():
    API_ENDPOINT = 'http://127.0.0.1:5000/v1/coviddata/'
    r = requests.get(url = API_ENDPOINT)
    data = r.json()
    try:
        results = data[str(sys.argv[1])]
        print(results)
    except IndexError:
        print('test exited with return=1')
        return 1
    print('test exited with return=0')
    return 0

if __name__ == "__main__":
    test()