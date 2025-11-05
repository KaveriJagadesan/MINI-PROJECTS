tasks = []

def display_menu():
    """Prints the menu options to the console."""
    print("\n==== To-Do List Menu ====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")
    print("=========================")

def add_task():
    """Prompts the user for a task and adds it to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    """Displays all tasks with their completion status."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "[ ] "
            if task.startswith("[X] "):
                status = ""
            print(f"{i}. {status}{task}")

def complete_task():
    """Marks a task as complete based on its number."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            # Check if the task is not already marked complete
            if not tasks[task_num - 1].startswith("[X] "):
                tasks[task_num - 1] = f"[X] {tasks[task_num - 1]}"
                print("Task marked as complete.")
            else:
                print("This task is already complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the command-line program."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
