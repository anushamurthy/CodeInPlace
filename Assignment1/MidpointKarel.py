from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

"""
Mid point Karel here has the following steps:
    # 1. Lay beepers on all except corners
    # 2. Go to either ends and pick up beepers iteratively until 
    you finish at the center 
    # 3. Place beeper at the center
    # 4. Exit

"""

def main():
    lay_beepers()
    find_mid_point()
    put_beeper()

"""Lay beepers is to put beepers on all points in the first row, except the corners
#pre: Facing east at the leftmost corner with no beepers present in the row.
#post: Facing west, placed at corner after the rightmost corner, with beepers in the entire row except corners."""

def lay_beepers():
        if front_is_blocked():
            turn_around()
        else:
            move()
            while front_is_clear():
                put_beeper()
                move()
            turn_around()
            move()

""" 
    Find midpoint moves to the last beeper in thr row of beepers 
    and picks up the beeper. It then turns back and continues until 
    no beepers are present. It stops finally at the center.
    pre: Starting end of row of beepers
    post: Center of the row.
"""

def find_mid_point():
        if front_is_blocked(): #This is when there is only 1 edge in the world, we turn around and do nothing.
            turn_around()
        else:
            while beepers_present():
                move_to_last_beeper()
                pick_beeper()
                move()
            turn_around()
            move()
""" 
    Move to Last Beeper function is to move until the last present 
    beeper in the row of beepers. 
    pre: Beginning end of row of beepers.
    post: Opposite end of row of beepers.
"""

def move_to_last_beeper():
    while beepers_present():
       move()
    turn_around()
    move()

""" 
    Turn around fucntion is to change the direction of Karel.
    pre: Faces east or west.
    post: Faces west or east.
"""
def turn_around():
        turn_left()
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
