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
            if split_input[0] != "task-cli":
                print("Invalid command format. Please start your command with 'task-cli'.")
                continue

            
            if command == "add":
                
                task_description = " ".join(split_input[2:])
                print(f"Adding a new task: {task_description}")
                add_task(task_description)
                continue

            elif command == "update":
                
                task_id = int(split_input[2])
                task_description = " ".join(split_input[3:])
                print(f"Updating task: {task_id}")
                update_task(task_id, task_description)  
                continue

            elif command == "delete":
                
                task_id = int(split_input[2])
                print(f"Deleting task: {task_id}")
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

