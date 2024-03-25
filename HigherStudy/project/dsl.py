import re

# Global lists to store tasks and completed tasks
tasks = []
completed_tasks = []

def handle_command(command):
    if command.startswith('+'):
        # Add a new task
        task_name = command[1:].strip()
        tasks.append(task_name)
        print(f"Added task: {task_name}")
    elif command.startswith('?'):
        # List all tasks
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        if completed_tasks:
            print("\nCompleted Tasks:")
            for i, task in enumerate(completed_tasks, 1):
                print(f"{i}. {task}")
    elif command.startswith('-'):
        # Remove a task by its number
        try:
            task_number = int(command[1:].strip()) - 1
            removed_task = tasks.pop(task_number)
            print(f"Removed task: {removed_task}")
        except (ValueError, IndexError):
            print("Invalid task number. Please enter a valid number.")
    elif command.startswith('x'):
        # Mark a task as completed
        try:
            task_number = int(command[1:].strip()) - 1
            completed_task = tasks.pop(task_number)
            completed_tasks.append(completed_task)
            print(f"Completed task: {completed_task}")
        except (ValueError, IndexError):
            print("Invalid task number. Please enter a valid number.")
    else:
        print("Unknown command.")

# Sample commands including removal and completion of tasks
commands = [
    "+ Learn Python",
    "+ Make dinner",
    "+ Read a book",
    "?",
    "- 2",  
    "x 1",
    "?"
]

for cmd in commands:
    handle_command(cmd)
