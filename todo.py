FILENAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # Agar file nahi hai toh ignore karna
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✔ Task added successfully!\n")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found!\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"✔ Removed task: {removed}\n")
    except (ValueError, IndexError):
        print("❌ Invalid input! Please try again.\n")


# Main menu

def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()