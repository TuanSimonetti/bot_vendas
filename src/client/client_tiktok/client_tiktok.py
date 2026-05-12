import requests


def client_tiktok_check(tiktok_client_key, tiktok_client_secret, tiktok_code, tiktok_url_redirect, tiktok_url_base):
    response = ""
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_key": tiktok_client_key,
        "client_secret": tiktok_client_secret,
        "code": tiktok_code,
        "grant_type": "authorization_code",
        "redirect_uri": tiktok_url_redirect
    }

    try:
        response = requests.post(tiktok_url_base, headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    finally:
        return response.json()
        #return token_data.get("access_token")
