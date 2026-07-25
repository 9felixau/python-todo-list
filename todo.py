# CLI Todo List Manager in Python

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def list_tasks():
    if not tasks:
        print("No tasks found.")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task index.")

if __name__ == "__main__":
    add_task("Buy groceries")