"""
This program is an assignment for MGTC28.
timer.py is a simple Python script for playing Nerve of Steel.
Nerve of Steel is a party game where players sit in a circle.  When the game begins:

1. The program displays "Players stand"

2. The program sleeps for a random time between 5 to 25 seconds.  While the program is sleeping, players can sit down.  Keep track of the last person to sit down.

3. When sleep is over, the program displays "Time Up.  Last to sit down wins."  Players still standing are eliminated, and the winner is the last person to sit down.
"""


# This program is for Nerve of Steel


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images
import random
im = Image.open("times-up.jpeg")

# displays "Players stand"
print("Players stand")

# sleeps for a random time between 5 to 25 seconds
time.sleep(random.randint(5, 25))

# program displays "Time Up.  Last to sit down wins."
print("Time up. Last to sit down wins.")

