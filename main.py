# Read official documentation here: https://developer.rocket.chat/reference/api/rest-api/endpoints/user-management/users-endpoints/get-users-info

import requests

# Define the API URL and headers
url = "http://localhost:3000/api/v1/users.info"
headers = {
    "X-Auth-Token": "LriN8m6slB0GpY5GUrcx3IizyTRUpIxWS21XEu37gl5",
    "Content-Type": "application/json",
    "X-User-Id": "k4vsvoirPcnvwkvrB"
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
    print(data, "\n")
    
    # Extract the 'lastLogin' parameter
    last_login = data.get('user', {}).get('lastLogin')
    
    if last_login:
        print("Last Login:", last_login)
    else:
        print("Last Login not found in the response.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
    print(response.text)