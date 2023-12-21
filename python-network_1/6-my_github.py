import requests
import sys

url = "https://api.github.com/user"
username = sys.argv[1]
password = sys.argv[2]

response = requests.get(url=url, auth=(username, password))
if response.status_code == 200:
    my_user_id = response.json()["id"]
    print(my_user_id)
else:
    print("None")

