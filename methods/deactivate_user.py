import requests
import os
from datetime import datetime

def deactivate_user(headers, payload, username):
    url = os.getenv("URL")+"/api/v1/users.setActiveStatus"
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            user = data.get('user')
            print("The user " + username + " has been deactivated.\n\n")
        else:
            print("Failed to set user status")
    else:
        print("Failed to deactivate user. Status code:", response.status_code)
        print(response.text)

def deactivated_users_list(deactivated_users):
    # current date for folder's name
    current_date = datetime.utcnow()

    # Check if the folder 'deactivated_users_lists' exists, and create it if it doesn't
    folder_path = 'deactivated_users_lists'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = f'deactivated_users_{current_date}.txt'
    file_path = os.path.join(folder_path, file_name)

    if deactivated_users:
        with open(file_path, 'w') as f:
            for user_id, (username, last_login_date) in deactivated_users.items():
                f.write(f"userID: {user_id}: username: '{username}', last_login_date: '{last_login_date}'\n")
        print("Deactivated users written to 'deactivated_users.txt'")

    # Print the dictionary of deactivated users
    print("\n\n\t\t ========= Deactivated Users: ========= \n\n")
    for user_id, (username, last_login_date) in deactivated_users.items():
        print(f"userID: {user_id}: username: '{username}', last_login_date: '{last_login_date}'")
    print("\n\n\t\t ========= Deactivated Users: ========= \n\n")