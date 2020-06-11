from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def main():
    turn_left() #To make Karel face upwards
    build()

"""
Build is the main function which restores the columns, crosses over to the 
next column and continues to restore it until no more columns are left.
pre: Bottom most edge of first column
post: Top most edge of last column
"""
def build():
    while right_is_clear():
        lay_column()
        climb_down()
        turn_left()
        cross_column()
        turn_left()
    lay_column()

"""
Lay column goes from bottom to top, while restoring the column.
It restores the column by placing beepers wherever beepers aren't present. 
pre: Bottom most edge of column - partially filled with beepers
post: Top most edge of same column - fully filled with beepers.
"""
def lay_column():
    while facing_north():
        if front_is_blocked():
            turn_around()
            restore()
        else:
            restore()
            move()

"""
Restore is to place beepers wherever beepers aren't present. 
If beepers are present, it skips to the next position.
"""
def restore():
    if no_beepers_present():
        put_beeper()

"""
Cross column is to cross over and go to the next column. 
It assumes that the columns are placed 4 positions apart.
pre: Bottom most edge of current column
post: Bottom most edge of adjacent column
"""

def cross_column():
    for i in range(4):
        move()

"""
Climb down is to make Karel climb down a column. 
pre: Top most coordinate of column
post: Bottom most coordinate of column
"""

def climb_down():
    while front_is_clear():
        move()

"""
Turn around
Change direction of Karel.
"""

def turn_around():
    turn_left()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
