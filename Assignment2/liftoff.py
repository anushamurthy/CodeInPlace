"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    countdown()

"""The function countdown counts down from 10 to 1 while printing the numbers and finally prints liftoff."""
def countdown():
    for i in range(10,0,-1):
        print (str(i))
    print("Liftoff!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
