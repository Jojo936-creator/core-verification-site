import os
from urllib.parse import urlencode

def handler(request):
    base_url = "https://apis.roblox.com/oauth/v1/authorize"
    params = {
        "response_type": "code",
        "client_id": os.getenv("CLIENT_ID"),
        "redirect_uri": os.getenv("REDIRECT_URI"),
        "scope": "openid"
    }

    redirect_url = f"{base_url}?{urlencode(params)}"
    return {
        "statusCode": 302,
        "headers": {
            "Location": redirect_url
        }
    }
