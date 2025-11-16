task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    if priority == "high":
        reminder += ". Try to complete it as soon as possible."
    elif priority == "medium":
        reminder += ". Consider completing it when you have time."
    else:
        reminder += ". Consider completing it when you have free time."
    print(f"Note: {reminder}")