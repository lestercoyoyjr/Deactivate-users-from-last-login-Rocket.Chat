import requests
import os
from dotenv import load_dotenv
from icecream import ic

def get_user_data(users_data):
    user_data_dict = {}  # Create an empty dictionary to store user data

    for user in users_data:
        user_id = user.get('_id')
        user_name = user.get('name')
        user_data_dict[user_id] = user_name

    return user_data_dict # Return the list of user data

def users_list():
    load_dotenv()

    url = os.getenv("URL")+"/api/v1/users.list"

    headers = {
        "X-Auth-Token": os.getenv("X-Auth-Token"),
        "X-User-Id": os.getenv("X-User-Id"),
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Check data
        # ic(data)

        # Extract 'id' values from the 'users' list
        usersData = data.get('users', [])
        user_data_dict = get_user_data(usersData)
        # Check Dictionary result
        # ic(user_data_dict)
        return user_data_dict
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        print(response.text)

# Test if it works
#if __name__ == "__main__":
#    users_list()