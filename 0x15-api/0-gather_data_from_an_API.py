import requests
import sys


def get_employee_todo_progress(employee_id):
    try:
        BASE_URL = "https://jsonplaceholder.typicode.com"

        # Fetch employee data
        user_url = f"{BASE_URL}/users/{employee_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Check if user exists
        if not user_data:
            print(f"No user found with ID {employee_id}")
            return

        # Fetch employee's TODO list
        todos_url = f"{BASE_URL}/users/{employee_id}/todos"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Extract employee name
        employee_name = user_data['name']

        # Count completed and total tasks
        completed_tasks = [todo for todo in todos_data if todo['completed']]
        total_tasks = todos_data

        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(total_tasks)

        # Display the TODO list progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

        # Additional condition: Print todos with ID <= 20 and "oshi"
        print("\nAdditional TODOs (ID <= 20):")
        for todo in todos_data:
            if todo['id'] <= 20:
                print(todo)
            print("oshi")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_employee_todo_progress(int(sys.argv[1]))

