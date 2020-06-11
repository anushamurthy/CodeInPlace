from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""
def main():
    put_beeper()
    while front_is_clear():
        climb_step()
        put_beeper()


def climb_step():
    move()
    move()
    turn_left()
    move()
    turn_right()



def main2():
    for i in range(3):
        paint_rectangle()

"""The function paint_rectangle will paint 3 sides of each 
rectangle. It paints 2 sides first and then paints the 3rd side, 
finally reorienting Karel to paint the next rectangle."""

def paint_rectangle():
    for i in range(2):
        paint_side()
        turn_left()
        move()
    paint_side()
    turn_right()

"""The function paint_side paints one side separately"""

def paint_side():
    while left_is_blocked():
        put_beeper()
        move()

"""This function is to make Karel turn right"""
def turn_right():
    for k in range (3):
      turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
