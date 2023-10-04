# Read official documentation here: https://developer.rocket.chat/reference/api/rest-api/endpoints/user-management/users-endpoints/get-users-info

import requests, os
from dotenv import load_dotenv
from datetime import datetime

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

# To deactivate user
payload = {
    'activeStatus': False,  # Set to False to deactivate the user
    'userId': '6Ft8E9onv5RjT7DNT',
    'confirmRelinquish': True
}


response = requests.get(url, headers=headers, params=query_params)

if response.status_code == 200:
    data = response.json()
    last_login = data.get('user', {}).get('lastLogin')
    username = data.get('user', {}).get('username')
    
    # Calculate the current date
    current_date = datetime.utcnow()
    
    last_login_date = datetime.strptime(last_login, '%Y-%m-%dT%H:%M:%S.%fZ')
    days_difference = (current_date - last_login_date).days
    
    if days_difference > 30: # could be any number
        user_input = input("The user " + username + " last login is older than 30 days. Do you want to deactivate this user? (yes/no): ")
        
        if user_input.lower() == "yes" or user_input.lower() == "y":
            # Code to deactivate the user
            url2 = "http://localhost:3000/api/v1/users.setActiveStatus"
            response2 = requests.post(url2, headers=headers, json=payload)
            if response2.status_code == 200:
                data = response2.json()
                if data.get('success'):
                    user = data.get('user')
                    print("The user " + username + " has been deactivated.")
                else:
                    print("Failed to set user status")
        else:
            print("The user " + username + " will not be deactivated.")
    else:
        print("The last login is not older than 30 days.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print(response.text)