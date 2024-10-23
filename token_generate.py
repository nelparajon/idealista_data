import json
import requests
import base64
from api_config import API_KEY, API_SECRET

def get_oauth_token():
    """Get the oath token for the Idealista API
    
    Args:
        None
    Return: 
        Token autehtication
    """
    
    message = f'{API_KEY}:{API_SECRET}'
    auth = "Basic " + base64.b64encode(message.encode("ascii")).decode("ascii")

    headers_dict = {
        "Authorization": auth,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }

    data = {
        "grant_type": "client_credentials",
        "scope": "read"
    }

    response = requests.post("https://api.idealista.com/oauth/token",
                  headers=headers_dict,
                  data=data)
    
    token = json.loads(response.text)["access_token"]
    return token

