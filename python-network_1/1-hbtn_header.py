"""importing requests and systems"""
import sys
import requests

"""taking a url using sys"""
url = input("enter url: ") if len(sys.argv) < 2 else sys.argv[1]

"""ruturning response from server"""
response = requests.get(url)

"""checking whether the variable is in the header"""
if 'X-Request-Id' in response.headers:
    value = response.headers['X-Request-Id']
    print(value)
