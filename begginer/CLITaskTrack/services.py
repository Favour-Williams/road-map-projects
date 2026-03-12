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

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updated_at"] = time.time()
            break
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
