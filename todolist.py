class Todo_list:
    def __init__(self):
        self.details = {}

    def add_task(self):
        self.task = input("Enter the task: ")
        self.deadline = input("Enter the deadline: ")
        self.details[self.task] = self.deadline
        self.prority = input("Enter the priority (High/Medium/Low): ")
        self.details[self.task] = (self.details[self.task], self.prority)
        self.projects = input("Enter the project name: ")
        self.details[self.task] = (self.details[self.task], self.projects) 
        print("Task added successfully.")   
    def view_tasks(self):
        if not self.details:
            print("No tasks found.")
        else:
            for task, status in self.details.items():
                print("Task:", task)
                print("Deadline:", status[0][0])
                print("Priority:", status[0][1])
                print("Project:", status[1])
                print("Status:", "Completed" if len(status) > 2 and status[2] == "Completed" else "Pending")

    def mark_completed(self):
        self.task = input("Enter the task to mark as completed: ")
        if self.task in self.details:
            self.details[self.task] = (self.details[self.task][0], self.details[self.task][1], "Completed")
            print("Task marked as completed.")
        else:
            print("Task not found.")
    def ext(self):
        print("Exiting the program.")
        exit()  
x = Todo_list()
while True:
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Mark Task as Completed")
    print("4.Exit")
    choice = int(input("Enter your choice: "))

    

    if choice == 1:
        x.add_task()
    elif choice == 2:
        x.view_tasks()
    elif choice == 3:
        x.mark_completed()
    elif choice == 4:
        x.ext()
          