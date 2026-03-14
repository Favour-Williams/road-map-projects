# 📋 CLI Task Tracker

A simple command-line interface (CLI) application for managing personal tasks. Track your to-do items, mark them as in progress or done, and keep everything organized in a JSON file.

## 🚀 Features

- ✅ Add new tasks with descriptions
- ✏️ Update existing task descriptions
- 🗑️ Delete tasks by ID
- 📝 List all tasks or filter by status (todo, in progress, done)
- 🔄 Mark tasks as in progress or done
- 💾 Persistent storage using JSON file

## 🛠️ Requirements

- Python 3.x
- No external dependencies required

## 📖 Usage

1. Run the application:
   ```bash
   python main.py
   ```
   or
   ```
   python3 main.py
   ```

3. Enter commands in the format: `task-cli <command> [arguments]`

### Available Commands

- **Add a task**: `task-cli add "Task description"`
- **Update a task**: `task-cli update <task_id> "New description"`
- **Delete a task**: `task-cli delete <task_id>`
- **List tasks**: `task-cli list` (lists all) or `task-cli list <status>` (e.g., `task-cli list todo`)
- **Mark in progress**: `task-cli mark-in-progress <task_id>`
- **Mark done**: `task-cli mark-done <task_id>`

### Examples

```
Enter a command (add, update, delete, list) or 'exit' to quit: task-cli add "Buy groceries"
Adding a new task: Buy groceries
Task added successfully: Buy groceries

Enter a command (add, update, delete, list) or 'exit' to quit: task-cli list
Listing all tasks...

ID: 1, Description: Buy groceries, Status: todo, Created At: Thu Mar 14 12:00:00 2026, Updated At: Thu Mar 14 12:00:00 2026

Enter a command (add, update, delete, list) or 'exit' to quit: task-cli mark-in-progress 1
Marking task 1 as in progress...
```

## 📄 File Structure

- `main.py`: Main CLI interface
- `services.py`: Task management functions
- `task.json`: JSON file storing tasks
- `README.md`: This file
