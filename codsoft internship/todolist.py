class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            print(f"Task '{self.tasks[index]}' marked as completed.")
            del self.tasks[index]
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            print(f"Task '{self.tasks[index]}' deleted.")
            del self.tasks[index]
        else:
            print("Invalid index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
