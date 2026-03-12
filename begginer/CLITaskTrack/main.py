from services import add_task, update_task, delete_task

def main():
    try:
        while True:
            user_input = input("Enter a command (add, update, delete, list) or 'exit' to quit: ")

            split_input = user_input.split()
            command = split_input[1] if split_input else ""
            

            if command not in ["add", "update", "delete", "list"]:
                print("Invalid command. Please enter 'add', 'update', 'delete', 'list', or 'exit'.")
                continue
            if command in ["add", "update", "delete"] and not task:
                print(f"Please provide a task description for the '{command}' command.")
                continue
            if split_input[0] != "task-cli":
                print("Invalid command format. Please start your command with 'task-cli'.")
                continue

            
            if command == "add":
                print(f"Adding a new task: {task}")
                task_description = " ".join(split_input[2:])
                add_task(task_description)
                continue

            elif command == "update":
                print(f"Updating task: {task}")
                task_id = int(split_input[2])
                task_description = " ".join(split_input[3:])
                update_task(task_id, task_description)  
                continue

            elif command == "delete":
                print(f"Deleting task: {task}")
                delete_task(task_id)  
                continue
            elif command == "list":
                print("Listing all tasks...")
                # Code to list tasks goes here
            elif user_input.lower() == "exit":
                print("Exiting the program.")
                break

            break  # Remove this line to keep the program running indefinitely
    except KeyboardInterrupt:
        print("Program ended by user.")

if __name__ == "__main__":
    main()

