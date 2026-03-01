"""
# Part 2:
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.
"""

try:
    # Get the current time and wait duration from the user
    current_time = int(input("Enter the current time (0-23): "))
    
    # Validate the current time is within the 24-hour range
    if current_time < 0 or current_time > 23:
        print("Error: Current time must be between 0 and 23.")
    else:
        hours_to_wait = int(input("Enter the number of hours to wait: "))

        # Validate that hours to wait is not negative
        if hours_to_wait < 0:
            print("Error: Hours to wait cannot be negative.")
        else:
            # Calculate the alarm time using modulo to wrap around the 24-hour clock
            alarm_time = (current_time + hours_to_wait) % 24

            # Display the result
            print(f"The alarm will go off at {alarm_time}:00 on a 24-hour clock.")

except ValueError:
    print("Error: Please enter a valid whole number.")