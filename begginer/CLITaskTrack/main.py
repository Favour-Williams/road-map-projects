from services import add_task

def main():
    try:
        while True:
            user_input = input("Enter a command (add, update, delete, list) or 'exit' to quit: ")

            split_input = user_input.split()
            command = split_input[1] if split_input else ""
            task = " ".join(split_input[2:]) if len(split_input) > 2 else ""

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
                add_task(task)
                if task: print(f"Task '{task}' added successfully.")
                continue

            elif command == "update":
                print(f"Updating task: {task}")
                # Code to update a task goes here
            elif command == "delete":
                print(f"Deleting task: {task}")
                # Code to delete a task goes here
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

