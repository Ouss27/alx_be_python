import datetime
from datetime import datetime, timedelta

#global variable
current_date = datetime.now() 

def display_current_datetime():
    # Get current date and time
    #current_date = datetime.now()

    # Format it to a specific format and print it
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_datetime)


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    duration = timedelta(days=number_of_days)
    future_date = current_date + duration

    # Create a timedelta object representing the duration
    #duration = timedelta(days=number_of_days)

    # Display the future date
    formatted_future_date = future_date.strftime("%y-%m-%d")
    print(f"Future date: {formatted_future_date}")




display_current_datetime()
calculate_future_date()