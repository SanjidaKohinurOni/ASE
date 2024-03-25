import re

# Global list to store tasks
tasks = []

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
    else:
        print("Unknown command.")

# Sample commands
commands = [
    "+ Learn Python",
    "+ Make dinner",
    "?"
]

for cmd in commands:
    handle_command(cmd)
