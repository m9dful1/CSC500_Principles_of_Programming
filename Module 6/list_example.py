task_list = ["Write discussion post", "Add new feature to project", "Do Zybooks chapter work"]

task_list.append("Commit feature to Github")   # Add new task to end
task_list.insert(2, "Fix bug in feature")      # Insert urgent task at index 2
task_list[0] = "Submit discussion post"        # Update existing task
task_list.pop(0)                               # Complete first task (removes it)
task_list.remove("Do Zybooks chapter work")    # Remove task by name

print(task_list)