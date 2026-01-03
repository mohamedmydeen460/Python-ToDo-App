tasks = []

while True:
    print("\n--- TO DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
