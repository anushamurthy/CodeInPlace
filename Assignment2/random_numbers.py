"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""
import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100
def main():
    generate_random()

"""The Generate_random function generates a random number between 0 to 100, and prints it. This is repeated 10 times."""
def generate_random():
    for i in range(NUM_RANDOM):
        x = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(str(x))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
