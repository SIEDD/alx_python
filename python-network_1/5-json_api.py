"""import requests and system packages"""
import sys
import requests

"""variables"""
url = sys.argv[1]
q = "" if len(sys.argv) < 2 else sys.argv[2]

data_to_send = {
    'q': q
}

response = requests.post(url=url, data=data_to_send)
try:
    check_json = response.json()
    if not check_json:
        print("No result")
    else:
        id = check_json.get("id")
        name = check_json.get("name")
        print(f"[{id}] {name}")
except ValueError:
    

