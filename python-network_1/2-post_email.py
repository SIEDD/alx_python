"""importing system and requests"""
import sys
import requests
"""variables that store url and email"""
url = input("enter URL: ") if len(sys.argv) < 2 else sys.argv[1]
email = input("enter email: ") if len(sys.argv) < 3 else sys.argv[2]

data = {
    'email':email
}
"""sending post to the url"""
response = requests.post(url=url, data=data)
print(response.text)