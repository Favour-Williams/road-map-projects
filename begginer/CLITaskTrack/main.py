from services import add_task, update_task, delete_task, list_tasks, mark_in_progress, mark_done

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
                if not task_description:
                    print("Error: Task description cannot be empty.")
                    continue
                print(f"Adding a new task: {task_description}")
                add_task(task_description)
                continue

            elif command == "update":
                
                task_id = int(split_input[2])
                task_description = " ".join(split_input[3:])
                if not task_description or task_id <= 0:
                    print("Error: Task ID must be a positive integer and description cannot be empty.")
                    continue
                print(f"Updating task: {task_id}")
                update_task(task_id, task_description)  
                continue

            elif command == "delete":
                
                task_id = int(split_input[2])
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer.")
                    continue
                print(f"Deleting task: {task_id}")
                delete_task(task_id)  
                continue

            elif command == "list":
                print("Listing all tasks...\n")
                ty = split_input[2] if len(split_input) > 2 else None
                list_tasks(ty)
                continue
                
            elif command == "mark-in-progress":
                task_id = int(split_input[2])
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer.")
                    continue
                print(f"Marking task {task_id} as in progress...")
                mark_in_progress(task_id)
                continue
                
            elif command == "mark-done":
                task_id = int(split_input[2])
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer.")
                    continue
                print(f"Marking task {task_id} as done...")
                mark_done(task_id)
                continue

            elif user_input.lower() == "exit":
                print("Exiting the program.")
                break

            break
    except KeyboardInterrupt:
        print("Program ended by user.")

if __name__ == "__main__":
    main()

