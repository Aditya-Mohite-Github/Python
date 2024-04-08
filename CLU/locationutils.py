import requests

def get_coordinates():
    req = requests.get('https://ipinfo.io/')
    return req.json()['loc']
    

