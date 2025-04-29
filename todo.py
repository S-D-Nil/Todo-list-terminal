import json
import argparse

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added: {task}")

def view_tasks():
    tasks = load_tasks()
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{idx}. [{status}] {task['task']}")

# Add more functions for delete, mark complete, etc.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    parser.add_argument("--add", help="Add a new task")
    parser.add_argument("--view", action="store_true", help="View all tasks")
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.view:
        view_tasks()
