import requests, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the API URL and headers
url = "http://localhost:3000/api/v1/users.info"
# Headers with authentication tokens
headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}

# Define the query parameter (in this case, 'username')
query_params = {
    "userId": "6Ft8E9onv5RjT7DNT"
}

# Make the GET request
response = requests.get(url, headers=headers, params=query_params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Check what data is coming in the GET call
    # print(data, "\n")
    
    # Extract the 'lastLogin' parameter
    last_login = data.get('user', {}).get('lastLogin')
    
    if last_login:
        print("Last Login:", last_login)
    else:
        print("Last Login not found in the response.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print(response.text)