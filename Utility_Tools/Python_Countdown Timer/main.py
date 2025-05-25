"""
Countdown Timer

Author: Abinash Prasana

This script takes a duration in seconds from the user and displays a real-time
countdown in HH:MM:SS format until the timer ends.
"""

import time

# Get input time in seconds
mt = int(input("Enter the countdown time in seconds: "))

# Countdown loop
for x in range(mt, 0, -1):
    # Convert total seconds to hours, minutes, seconds
    sec = x % 60
    min = int(x / 60) % 60
    hour = int(x / 3600)

    # Print time in HH:MM:SS format
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("Time's Up")