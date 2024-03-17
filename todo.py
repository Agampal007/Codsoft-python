import os

class TodoList:
    def __init__(self, filename="todolist.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    title, status = line.strip().split(',')
                    tasks.append({'title': title, 'done': status == 'Done'})
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                status = 'Done' if task['done'] else 'Not done'
                file.write(f"{task['title']},{status}\n")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['title']} - {'Done' if task['done'] else 'Not done'}")

    def add_task(self, title):
        task = {'title': title, 'done': False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def update_task(self, task_index, new_title):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['title'] = new_title
            self.save_tasks()
            print(f"Task {task_index} updated successfully.")
        else:
            print("Invalid task index.")

    def toggle_task_status(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['done'] = not self.tasks[task_index - 1]['done']
            self.save_tasks()
            print(f"Task {task_index} status toggled.")
        else:
            print("Invalid task index.")

    def run(self):
        while True:
            print("\n=== ToDo List ===")
            print("1. Display tasks")
            print("2. Add task")
            print("3. Update task")
            print("4. Toggle task status")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                title = input("Enter task title: ")
                self.add_task(title)
            elif choice == '3':
                task_index = int(input("Enter task index to update: "))
                new_title = input("Enter new task title: ")
                self.update_task(task_index, new_title)
            elif choice == '4':
                task_index = int(input("Enter task index to toggle status: "))
                self.toggle_task_status(task_index)
            elif choice == '5':
                print("Exiting ToDo List. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()
