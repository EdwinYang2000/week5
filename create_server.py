import requests

url = 'http://127.0.0.1:5000/servers/'

def create_server(name,host):
    data = {
            'name': name,
            'host': host
            }
    r = requests.post(url,json=data)
    return r.json()

