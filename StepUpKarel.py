from karel.stanfordkarel import *

"""
File: StepUpKarel.py
----------------------------

Karel completes a puzzle by:
1. Karel move farward.
2. Pick up the beeper.
3. Karel move forward till hit the wall.
4. Karel turn left.
5. Karel move forward.
6. turn right.
7. Karel move forward.
8. Put down the beeper.
9. Karel moves forward till hit the wall.
"""
def main():
    move_and_grab_beepers()
    face_north()
    step_up()
    move_and_put_beepers()

def move_and_put_beepers():
    move_safely()
    put_beeper()
    move_forward()

def step_up():
    face_north()
    move_safely()
    face_east()

def face_east():
    while not facing_east():
        turn_left()

def move_and_grab_beepers():
    while front_is_clear():
        grab_beeper()
        move_safely()


def grab_beeper():
    while beepers_present():
        pick_beeper()

def move_forward():
    while front_is_clear():
        move_safely()

def face_north():
    while not facing_north():
        turn_left()

def move_safely():
    if front_is_clear():
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
