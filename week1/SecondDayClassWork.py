#username
#email
#company

import requests

userid=6
URL = f"https://jsonplaceholder.typicode.com/users/{userid}"
for i in range(1, 11):
    URL = f"https://jsonplaceholder.typicode.com/users/{i}"
    response = requests.get(URL)
    print(f"Response status code: {response.status_code}")

    data = response.json()
    print(f"User ID: {data['id']}")
    print(f"Username: {data['username']}")
    print(f"Email: {data['email']}")
    print(f"Company: {data['company']['name']}")
    print(f"phone: {data['phone']}")
    if(len(data['phone'].split('x'))>1):
        if(len(data['phone'].split('x')[1])>0):
            print(f"Extension: {data['phone'].split('x')[1]}")
    print("================================")
# print(data)