import datetime
from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()

    # Format it to a specific format and print it
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_datetime)

    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # Create a timedelta object representing the duration
    duration = timedelta(days=number_of_days)

    # Add the timedelta to the current date
    future_date = current_date + duration

    # Display the future date
    formatted_future_date = future_date.strftime("%y-%m-%d")
    print(f"Future date: {formatted_future_date}")




display_current_datetime()