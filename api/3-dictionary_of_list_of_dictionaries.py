import json
import requests

def get_employee_info(employee_id):
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    completed_tasks = [{'username': employee_data['username'], 'task': task['title'], 'completed': task['completed']} for task in todos_data]

    return completed_tasks

def export_all_tasks():
    all_employees_tasks = {}

    for employee_id in range(1, 11):
        all_employees_tasks[str(employee_id)] = get_employee_info(employee_id)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

if __name__ == "__main__":
    export_all_tasks()
