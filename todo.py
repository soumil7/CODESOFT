class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def update_task(self, task_number, new_task):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task number.")

if __name__ == "__main__":
    todo_list = ToDoList()

    print("Welcome to the To-Do List App!\n")
    print("Commands:")
    print("- add: Add a new task")
    print("- view: View the list of tasks")
    print("- update: Update a task")
    print("- delete: Delete a task")
    print("- exit: Exit the application\n")

    while True:
        command = input("Enter command: ").lower()

        if command == "add":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif command == "view":
            todo_list.view_tasks()
        elif command == "update":
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(task_number, new_task)
        elif command == "delete":
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif command == "exit":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")
