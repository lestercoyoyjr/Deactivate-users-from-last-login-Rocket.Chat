import requests

def deactivate_user(headers, payload, username):
    url = "http://localhost:3000/api/v1/users.setActiveStatus"
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
    if deactivated_users:
        with open('deactivated_users.txt', 'w') as f:
            for user_id, (username, last_login_date) in deactivated_users.items():
                f.write(f"userID: {user_id}: username: '{username}', last_login_date: '{last_login_date}'\n")
        print("Deactivated users written to 'deactivated_users.txt'")

    # Print the dictionary of deactivated users
    print("Deactivated Users:")
    for user_id, (username, last_login_date) in deactivated_users.items():
        print(f"userID: {user_id}: username: '{username}', last_login_date: '{last_login_date}'")