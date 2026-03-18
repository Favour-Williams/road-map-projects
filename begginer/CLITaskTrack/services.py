"""
Task Management Services

This module provides functions for managing tasks stored in a JSON file.
It handles CRUD operations and status updates for tasks.
"""

import json
import time
from typing import List, Dict, Optional

# Constants
TASK_STATUSES = ["todo", "in-progress", "done"]
TASK_FILE = "task.json"

def load_tasks() -> List[Dict]:
    """
    Load tasks from the JSON file.

    Returns:
        List of task dictionaries. Returns empty list if file doesn't exist.
    """
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in task file. Starting with empty task list.")
        return []

def save_tasks(tasks: List[Dict]) -> None:
    """
    Save tasks to the JSON file.

    Args:
        tasks: List of task dictionaries to save.
    """
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_description: str) -> None:
    """
    Add a new task to the task list.

    Args:
        task_description: Description of the task to add.
    """
    if not task_description.strip():
        print("Error: Task description cannot be empty.")
        return

    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": task_description.strip(),
        "status": "todo",
        "created_at": time.time(),
        "updated_at": time.time()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']}): {task_description}")

def update_task(task_id: int, new_description: str) -> None:
    """
    Update the description of an existing task.

    Args:
        task_id: ID of the task to update.
        new_description: New description for the task.
    """
    if not new_description.strip():
        print("Error: Task description cannot be empty.")
        return

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description.strip()
            task["updated_at"] = time.time()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return

    print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id: int) -> None:
    """
    Delete a task by its ID.

    Args:
        task_id: ID of the task to delete.
    """
    tasks = load_tasks()
    original_count = len(tasks)

    # Filter out the task to delete
    filtered_tasks = [task for task in tasks if task["id"] != task_id]

    if len(filtered_tasks) == original_count:
        print(f"Error: Task with ID {task_id} not found.")
    else:
        save_tasks(filtered_tasks)
        print(f"Task {task_id} deleted successfully.")

def list_tasks(status_filter: Optional[str] = None) -> None:
    """
    List tasks, optionally filtered by status.

    Args:
        status_filter: Optional status to filter by ('todo', 'in progress', 'done').
    """
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    if status_filter:
        if status_filter not in TASK_STATUSES:
            print(f"Error: Invalid status '{status_filter}'. Valid statuses: {', '.join(TASK_STATUSES)}")
            return
        print(f"Tasks with status '{status_filter}':\n")
        tasks = [task for task in tasks if task["status"] == status_filter]
    else:
        print("All tasks:\n")

    if not tasks:
        print("No tasks match the specified criteria.")
        return

    for task in tasks:
        created_time = time.ctime(task['created_at'])
        updated_time = time.ctime(task['updated_at'])
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created: {created_time}")
        print(f"Updated: {updated_time}")
        print("-" * 40)

def mark_in_progress(task_id: int) -> None:
    """
    Mark a task as in progress.

    Args:
        task_id: ID of the task to mark.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in progress"
            task["updated_at"] = time.time()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in progress.")
            return

    print(f"Error: Task with ID {task_id} not found.")

def mark_done(task_id: int) -> None:
    """
    Mark a task as done.

    Args:
        task_id: ID of the task to mark.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updated_at"] = time.time()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return

    print(f"Error: Task with ID {task_id} not found.")