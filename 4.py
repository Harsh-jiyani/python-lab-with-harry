import time

# Get the current hour
current_hour = int(time.strftime('%H'))

# Determine the greeting based on the hour
if 5 <= current_hour < 12:
    greeting = "Good morning"
elif 12 <= current_hour < 17:
    greeting = "Good afternoon"
elif 17 <= current_hour < 21:
    greeting = "Good evening"
else:
    greeting = "Good night"

print(greeting)
