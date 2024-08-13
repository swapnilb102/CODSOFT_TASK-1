import json

class ToDoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            self.save_tasks()
        else:
            print("Invalid task number.")

    def mark_task_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Mark a task as done")
        print("5. Delete a task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_done(task_number)
        elif choice == "5":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
