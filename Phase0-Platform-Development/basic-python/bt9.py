tasks = []

def add_task(title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)

def show_tasks():
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not done"
        print(index + 1, task["title"], "-", status)

add_task("Hoc Python")
add_task("Lam bai tap")
show_tasks()