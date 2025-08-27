import os
import requests

def exchange_code_for_token(code):
    token_url = "https://apis.roblox.com/oauth/v1/token"
    data = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": os.getenv("REDIRECT_URI")
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(token_url, data=data, headers=headers)
    print("Status:", response.status_code)
    print("Text:", response.text)  

    return response.json()
