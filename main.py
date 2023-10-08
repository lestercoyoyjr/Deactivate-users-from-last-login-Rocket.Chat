# Read official documentation here: https://developer.rocket.chat/reference/api/rest-api/endpoints/user-management/users-endpoints/get-users-info

import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from difference_days import difference_days
from deactivate_user import deactivate_user

def main():
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
        last_login = data.get('user', {}).get('lastLogin')
        username = data.get('user', {}).get('username')

        # Calculate the current date
        days_difference = difference_days(last_login)

        if days_difference > 30:  # could be any number
            user_input = input(
                "The user " + username + " last login is older than 30 days. Do you want to deactivate this user? (yes/no): ")

            if user_input.lower() == "yes" or user_input.lower() == "y":
                # Code to deactivate the user
                payload = {
                    'activeStatus': False,  # Set to False to deactivate the user
                    'userId': '6Ft8E9onv5RjT7DNT',
                    'confirmRelinquish': True
                }
                deactivate_user(headers, payload, username)
            else:
                print("The user " + username + " will not be deactivated.")
        else:
            print("The last login is not older than 30 days.")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    main()