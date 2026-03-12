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