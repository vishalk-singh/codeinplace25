from CollectNewspaperKarel import turn_around
from karel.stanfordkarel import *

"""
File: Spreadbeeper8x1.py
----------------------------
In this task, Karel will always start by standing in front of a pile of beepers. 
Karel needs to pick up the entire pile of beepers and spread them out along the row 
so that there is exactly one beeper in each cell, 
and exactly as many cells with beepers as were in the original pile. 
The line of spread beepers should begin where the pile originated (which is on row 1 column 2).
You may assume that:
1. There is only one row in the world
2. Karel starts with infinite beepers in her bag (how will you make sure to only spread as many beepers as were in the original pile?)
3. The pile of beepers is on the second corner, directly in front of where Karel starts
4. The world is wide enough for all the beepers, and there will be empty cells at the end of the row at the end

Write the code to implement Spread Beepers Karel. 
    1. Come up with a strategy first. 
    2.Think, "what are the high-level steps Karel needs to take?" 
      and make these steps into helper functions. 
    3. Remember that your program should work for a pile of any size.
"""
def main():
    move()
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_till_end_of_beeper()
            put_beeper()
            move_to_the_pile()
    put_beeper()
    go_home()

def go_home():
    turn_around()
    move_to_wall()
    turn_around()

def move_to_the_pile():
    turn_around()
    move_to_wall()
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def move_till_end_of_beeper():
    while beepers_present():
        move()

# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
