import json
import argparse
from pathlib import Path

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file. Return empty list if file doesn't exist."""
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"✓ Added: '{description}'")

def view_tasks():
    """Display all tasks with their status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet! Add one with '--add'.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['description']}")
    print()

def mark_task_done(task_num):
    """Mark a task as done."""
    tasks = load_tasks()
    try:
        task_num = int(task_num) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            save_tasks(tasks)
            print(f"✓ Marked task {task_num + 1} as done!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid task number.")

def delete_task(task_num):
    """Delete a task."""
    tasks = load_tasks()
    try:
        task_num = int(task_num) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"✓ Deleted: '{removed['description']}'")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid task number.")

def main():
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    parser.add_argument("--add", help="Add a new task")
    parser.add_argument("--view", action="store_true", help="View all tasks")
    parser.add_argument("--done", help="Mark a task as done (provide task number)")
    parser.add_argument("--delete", help="Delete a task (provide task number)")
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.view:
        view_tasks()
    elif args.done:
        mark_task_done(args.done)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    # Create tasks file if it doesn't exist
    Path(TASKS_FILE).touch(exist_ok=True)
    main()
