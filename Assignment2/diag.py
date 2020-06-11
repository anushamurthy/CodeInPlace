"""
File: moon_weight.py
--------------------
Add your comments here.
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    return n  #Return the n value back to the main program

def main():
    print("Enter a sequence of non-decreasing numbers.")
    count = 0
    x = float(input("Enter a number"))
    y = x
    while x >= y:
        y = x
        x = float(input("Enter a number"))
        count = count + 1
    print("Thanks for playing. Sequence length =" + str(count))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
