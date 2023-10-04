import requests, os
from dotenv import load_dotenv

load_dotenv()

url = "http://localhost:3000/api/v1/users.info"

headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}

query_params = {
    "userId": "6Ft8E9onv5RjT7DNT"
}

response = requests.get(url, headers=headers, params=query_params)

if response.status_code == 200:
    data = response.json()
    username = data.get('user', {}).get('username')

    print("Username:", username)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print(response.text)