import requests


def client_instagram_check(user_id, access_token):
    response = ""
    # Endpoint para buscar informações do perfil
    url = f"https://graph.facebook.com/v22.0/{user_id}?fields=username,media_count&access_token={access_token}"

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    finally:
        data = response.json()
        return f"User: {data['username']} | Posts: {data['media_count']}"
