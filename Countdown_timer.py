import time  # Import time module for time-related operations

def countdown(seconds):  # Function definition
    while seconds > 0:  # Continue while seconds is greater than zero
        print(f"Time remaining: {seconds} seconds")  # Print remaining time
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease seconds by 1
    print("⏰ Time's up!")  # Message when countdown finishes

print("⏳ Countdown Timer")  # Title
try:
    duration = int(input("How many seconds do you want to count? "))  # Get user input
    countdown(duration)  # Call the function
except ValueError:
    print("Please enter numbers only!")  # Warning on invalid input
