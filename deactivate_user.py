import requests

def deactivate_user(headers, payload, username):
    url = "http://localhost:3000/api/v1/users.setActiveStatus"
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            user = data.get('user')
            print("The user " + username + " has been deactivated.")
        else:
            print("Failed to set user status")
    else:
        print("Failed to deactivate user. Status code:", response.status_code)
        print(response.text)