import os
import json
from datetime import datetime

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_index):
        del self.tasks[task_index]
        self.save_tasks()

    def mark_task_completed(self, task_index):
        self.tasks[task_index]['completed'] = True
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("Tasks:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{index + 1}. {task['description']} (Priority: {task['priority']}, Due: {task['due_date']}, Status: {status})")

def get_input(prompt):
    return input(prompt).strip()

def main():
    task_manager = TaskManager()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = get_input("Enter your choice: ")

        if choice == "1":
            description = get_input("Enter task description: ")
            priority = get_input("Enter priority (high, medium, low): ")
            due_date = get_input("Enter due date (YYYY-MM-DD): ")
            task = {
                'description': description,
                'priority': priority,
                'due_date': due_date,
                'completed': False
            }
            task_manager.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            task_manager.list_tasks()
            if task_manager.tasks:
                task_index = int(get_input("Enter task number to remove: ")) - 1
                if 0 <= task_index < len(task_manager.tasks):
                    task_manager.remove_task(task_index)
                    print("Task removed successfully.")
                else:
                    print("Invalid task number.")
        
        elif choice == "3":
            task_manager.list_tasks()
            if task_manager.tasks:
                task_index = int(get_input("Enter task number to mark as completed: ")) - 1
                if 0 <= task_index < len(task_manager.tasks):
                    task_manager.mark_task_completed(task_index)
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
        
        elif choice == "4":
            task_manager.list_tasks()

        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
