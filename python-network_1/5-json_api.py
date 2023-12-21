"""import requests and system packages"""
import sys
import requests

"""variables"""
url = "http://0.0.0.0:5000/search_user"
q = "" if len(sys.argv) ==1 else sys.argv[1]

data_to_send = {
    'q': q
}

response = requests.post(url=url, data=data_to_send)
try:
    check_json = requests.json()
    if not check_json:
        print("No result")
    else:
        id = check_json.get("id")
        name = check_json.get("name")
        print(f"[{id}] {name}")
except ValueError:
    print("Not a valid JSON")
    

