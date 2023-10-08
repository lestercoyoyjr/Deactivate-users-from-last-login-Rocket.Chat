import requests

def username_get(response):
    data = response.json()
    last_login = data.get('user', {}).get('lastLogin')
    username = data.get('user', {}).get('username')
    return last_login, username