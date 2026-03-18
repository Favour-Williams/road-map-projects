"""
CLI Task Tracker - Main Entry Point

This module provides a command-line interface for managing tasks.
It handles user input, parses commands, and delegates operations to the services module.
"""

from services import add_task, update_task, delete_task, list_tasks, mark_in_progress, mark_done

def main():
    """
    Main function that runs the CLI task tracker application.
    Handles user input in a loop until the user chooses to exit.
    """
    print("Welcome to the CLI Task Tracker!")
    print("Enter commands in the format: task-cli <command> [arguments]")
    print("Type 'exit' to quit.\n")

    try:
        while True:
            # Get user input
            user_input = input("Enter a command: ").strip()

            # Handle exit command
            if user_input.lower() == "exit":
                print("\nExiting the program. Goodbye!")
                break

            # Split input into parts
            split_input = user_input.split()
            if len(split_input) < 2:
                print("Invalid command format. Please use: task-cli <command> [arguments]")
                continue

            # Validate command prefix
            if split_input[0] != "task-cli":
                print("Invalid command format. Please start with 'task-cli'.")
                continue

            # Extract command
            command = split_input[1]

            # Validate command
            valid_commands = ["add", "update", "delete", "list", "mark-in-progress", "mark-done"]
            if command not in valid_commands:
                print(f"Invalid command '{command}'. Valid commands: {', '.join(valid_commands)}")
                continue

            # Handle 'add' command
            if command == "add":
                if len(split_input) < 3:
                    print("Error: Please provide a task description.")
                    continue
                task_description = " ".join(split_input[2:])
                print(f"Adding task: {task_description}")
                add_task(task_description)

            # Handle 'update' command
            elif command == "update":
                if len(split_input) < 4:
                    print("Error: Please provide task ID and new description.")
                    continue
                try:
                    task_id = int(split_input[2])
                    if task_id <= 0:
                        raise ValueError
                    task_description = " ".join(split_input[3:])
                    print(f"Updating task {task_id}: {task_description}")
                    update_task(task_id, task_description)
                except ValueError:
                    print("Error: Task ID must be a positive integer.")

            # Handle 'delete' command
            elif command == "delete":
                if len(split_input) < 3:
                    print("Error: Please provide task ID.")
                    continue
                try:
                    task_id = int(split_input[2])
                    if task_id <= 0:
                        raise ValueError
                    print(f"Deleting task {task_id}")
                    delete_task(task_id)
                except ValueError:
                    print("Error: Task ID must be a positive integer.")

            # Handle 'list' command
            elif command == "list":
                status_filter = split_input[2] if len(split_input) > 2 else None
                print("Listing tasks...")
                list_tasks(status_filter)

            # Handle 'mark-in-progress' command
            elif command == "mark-in-progress":
                if len(split_input) < 3:
                    print("Error: Please provide task ID.")
                    continue
                try:
                    task_id = int(split_input[2])
                    if task_id <= 0:
                        raise ValueError
                    print(f"Marking task {task_id} as in progress...")
                    mark_in_progress(task_id)
                except ValueError:
                    print("Error: Task ID must be a positive integer.")

            # Handle 'mark-done' command
            elif command == "mark-done":
                if len(split_input) < 3:
                    print("Error: Please provide task ID.")
                    continue
                try:
                    task_id = int(split_input[2])
                    if task_id <= 0:
                        raise ValueError
                    print(f"Marking task {task_id} as done...")
                    mark_done(task_id)
                except ValueError:
                    print("Error: Task ID must be a positive integer.")

    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")

if __name__ == "__main__":
    main()

