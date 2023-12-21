"""Import request"""
import requests

"""Takes the url and request it is using to get the method"""

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: OK".format(response.text))

