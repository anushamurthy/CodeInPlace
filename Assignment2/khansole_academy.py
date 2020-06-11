"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

RIGHT_SCORE = 3
RANDOM_MIN = 10
RANDOM_MAX = 99

def main():
    test()

"""The function test begins with your score being 0. The users are continued to be tested until 
their score matches the right score (which is 3 here). The user wins a score if they enter the correct 
total of 2 random numbers. If they don't get the total right, score resets and test continues."""

def test():
    score = 0
    while score < RIGHT_SCORE:
        actual_total,entered_total = generate_random()
        if actual_total == entered_total:
            score = score + 1
            print("Correct! You've gotten " + str(score) + " correct in a row")
        else:
            print("Incorrect. The expected answer is " + str(actual_total))
            score = 0
    print("Congratulations, you've mastered addition.")

""" Generate random function generates 2 random numbers num1 & num2 between a specified maximum and minimum value. 
It asks the users to sum up those 2 numbers. It then returns the entered sum and also the actual sum of the 2 numbers. """

def generate_random():
    num1 = random.randint(RANDOM_MIN, RANDOM_MAX)
    num2 = random.randint(RANDOM_MIN, RANDOM_MAX)
    actual_total = num1 + num2
    entered_total = int(input("What is " + str(num1) + " + " + str(num2) + "? "))
    return actual_total, entered_total

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
