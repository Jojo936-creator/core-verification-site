import os
import requests
from urllib.parse import parse_qs

def handler(request):
    query_params = parse_qs(request["queryStringParameters"])
    code = query_params.get("code", [None])[0]

    if not code:
        return {
            "statusCode": 400,
            "body": "Missing code"
        }

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
    if response.status_code != 200:
        return {
            "statusCode": 400,
            "body": f"Token request failed: {response.text}"
        }

    tokens = response.json()
    access_token = tokens.get("access_token")

    userinfo_response = requests.get(
        "https://apis.roblox.com/oauth/v1/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    user_data = userinfo_response.json()
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": str(user_data)
    }
