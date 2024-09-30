import datetime
from datetime import datetime, timedelta

# Get current date and time
current_date = datetime.now() #global variable

#Part1 : Display the Current Date and Time
def display_current_datetime():
    # Format it to a specific format and print it
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time: ", formatted_datetime)

#Part2 : Calculate a Future Date
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    #creating a timedelta object and storing it in the variable duration
    duration = timedelta(days=number_of_days)

    #calculate future date
    future_date = current_date + duration

    # Format it to specific format and Display it
    formatted_future_date = future_date.strftime("%y-%m-%d")
    print(f"Future date: {formatted_future_date}")




display_current_datetime()
calculate_future_date()