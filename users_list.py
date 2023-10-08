import requests
import os
from dotenv import load_dotenv
from icecream import ic

def users_list():
    load_dotenv()

    url = "http://localhost:3000/api/v1/users.list"

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
        ic(data)

        # Extract 'id' values from the 'users' list
        users_data = data.get('users', [])
        for user in users_data:
            user_id = user.get('_id')
            user_name = user.get('name')
            print("User ID: "+ user_id + ", User Name:" + user_name + ",")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        print(response.text)


if __name__ == "__main__":
    users_list()
