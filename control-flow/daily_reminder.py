task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

reminder = ""
match priority:
    case "high":
        reminder += f"'{task}' is a {priority} priority task"

    case "medium":
        reminder += f"'{task}' is a {priority} priority task"

    case "low":
        reminder += f"'{task}' is a {priority} priority task"

if time_bound == "yes" or priority == "high":
    print(f"Reminder: {reminder} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: {reminder}. Consider completing it when you have free time.")
       
#Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
#Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
