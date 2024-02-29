"""importing libraries"""
import json
import requests
import sys
"""employee informatiom"""
def get_employee_info(employee_id):
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    """url, response and data"""
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    """file path"""
    json_file_path = f"{employee_id}.json"
    json_data = {
        f"{employee_id}": [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_data['username']
            }
            for task in todos_data
        ]
    }

    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

if __name__ == "__main__":
    get_employee_info(sys.argv[1])
