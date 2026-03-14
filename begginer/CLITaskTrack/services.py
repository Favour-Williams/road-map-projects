import json
import time

task_statuses = ["todo", "in progress", "done"]
def load_tasks():
    try:
        with open("task.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_task(task_description):
    tasks = load_tasks()
    tasks.append({
        "id": len(tasks) + 1, 
        "description": task_description,
        "status": "todo", 
        "created_at": time.time(), 
        "updated_at": time.time()
    })
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)
    if task_description:
        print(f"Task added successfully: {task_description}")
    else:
        print("Error: Task description cannot be empty.")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = time.time()
            break
    if task_id > len(tasks) or task_id <= 0:
        print(f"Error: Task ID {task_id} not found.")
    
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

def delete_task(task_id):
    tasks = load_tasks()
    original_count = len(tasks)
    
    filtered_tasks = [task for task in tasks if task["id"] != task_id]
    
    if len(filtered_tasks) == original_count:
        print(f"Error: Task ID {task_id} not found.")
    else:
        with open("task.json", "w") as file:
            json.dump(filtered_tasks, file, indent=4)
        print(f"Task {task_id} deleted successfully.")

def list_tasks(ty=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    task_types = ["todo", "in progress", "done"]
    if ty and ty in task_types:
        print(f"Listing tasks with status: {ty}\n")
        tasks = [task for task in tasks if task["status"] == ty]
    
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {time.ctime(task['created_at'])}, Updated At: {time.ctime(task['updated_at'])}\n")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in progress"
            task["updated_at"] = time.time()
            break
    if task_id > len(tasks) or task_id <= 0:
        print(f"Error: Task ID {task_id} not found.")
    
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updated_at"] = time.time()
            break
    if task_id > len(tasks) or task_id <= 0:
        print(f"Error: Task ID {task_id} not found.")
    
    with open("task.json", "w") as file:
        json.dump(tasks, file, indent=4)