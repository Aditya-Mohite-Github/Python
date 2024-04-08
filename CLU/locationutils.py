# Import the requests module to make HTTP requests
import requests

# Define a function named get_coordinates
def get_coordinates():
    # Send a GET request to 'https://ipinfo.io/' to retrieve information about the IP address
    req = requests.get('https://ipinfo.io/')
    
    # Return the latitude and longitude coordinates extracted from the JSON response
    return req.json()['loc']
