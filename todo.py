# CLI Todo List Manager in Python

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def list_tasks():
    if not tasks: