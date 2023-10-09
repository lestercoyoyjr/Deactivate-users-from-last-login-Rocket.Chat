# Read official documentation here: https://developer.rocket.chat/reference/api/rest-api/endpoints/user-management/users-endpoints

import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from methods.difference_days import difference_days
from methods.deactivate_user import deactivate_user, deactivated_users_list
from methods.username import username_get
from methods.users_list import users_list


load_dotenv()

url = "http://localhost:3000/api/v1/users.info"

headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}

user_data_dict = users_list()
deactivated_users = {}  # Create an empty dictionary to store deactivated users

# Process each user in the dictionary
while user_data_dict:
    user_id, username = user_data_dict.popitem()
    query_params = {
        "userId": user_id
    }

    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code == 200:
        last_login, username = username_get(response)

        # Calculate the current date
        days_difference = difference_days(last_login)

        if days_difference is None:
            # Skip processing this user if days_difference is None
            print("The user " + username + " has never logged in")
            continue

        if days_difference > 30:  # could be any number
            user_input = input(
                "\n\nThe user " + username + " last login is older than 30 days (Last Login: "+ last_login +"). Do you want to deactivate this user? (yes/no): ")

            if user_input.lower() == "yes" or user_input.lower() == "y":
                # Code to deactivate the user
                payload = {
                    'activeStatus': False,  # Set to False to deactivate the user
                    'userId': user_id,
                    'confirmRelinquish': True
                }
                deactivate_user(headers, payload, username)
                # Add the deactivated user to the dictionary
                deactivated_users[user_id] = username, last_login
            else:
                print("The user " + username + " will not be deactivated.\n\n")
        else:
            print("\n\nIMPORTANT: The user " + username + " last login is not older than 30 days.\n\n")
    else:
        print("Failed to retrieve data for user", username, ". Status code:", response.status_code)
        print(response.text)


# Check if deactivated_users is not empty and write it to a .txt file
if deactivated_users:
    deactivated_users_list(deactivated_users)
