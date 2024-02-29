import requests
import sys

def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_info(employee_id)
