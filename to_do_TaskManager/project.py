# Features
# Add Task
# View Task
# Delete Task
# Exit Task

tasks = []

def addTask():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully\n")

def viewTasks():
    if len(tasks) == 0:
        print("No tasks available\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)

def deleteTask():
    viewTasks()
    
    if len(tasks) == 0:
        return
    
    num = int(input("Enter task number to delete: "))
    
    if num > 0 and num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted successfully\n")
    else:
        print("Invalid task number\n")

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addTask()

    elif choice == "2":
        viewTasks()

    elif choice == "3":
        deleteTask()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")