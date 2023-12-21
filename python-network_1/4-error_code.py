# import sys
# import requests

# url = sys.argv[1]
# if status_code >=400:
#     print("error code: ")
import requests
import sys

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # If successful, print the response content
        print(response.text)
    except requests.exceptions.HTTPError as err:
        # If there's an HTTP error, print the error code
        print(f"Error code: {err.response.status_code}")
    except requests.exceptions.RequestException as e:
        # For other request errors, print a generic error message
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    fetch_url(url)
