task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

if time_bound == "yes" or priority == "high":
    reminder = "Reminder: "
else:
    reminder = "Note: "

match priority:
    case "high":
        reminder += f"'{task}' is a {priority} priority task"

    case "medium":
        reminder += f"'{task}' is a {priority} priority task"

    case "low":
        reminder += f"'{task}' is a {priority} priority task"

if time_bound == "yes" or priority == "high":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
       

print (reminder)
