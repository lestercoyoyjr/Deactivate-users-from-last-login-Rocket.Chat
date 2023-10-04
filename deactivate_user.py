import requests, os
from dotenv import load_dotenv

load_dotenv()

url = "http://localhost:3000/api/v1/users.setActiveStatus"

headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}

payload = {
    'activeStatus': True,  # Set to False to deactivate the user
    'userId': '6Ft8E9onv5RjT7DNT',
    'confirmRelinquish': True
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    if data.get('success'):
        user = data.get('user')
        print(f"User with ID {user['_id']} is now active: {user['active']}")
    else:
        print("Failed to set user status")
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)