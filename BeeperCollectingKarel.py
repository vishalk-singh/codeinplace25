"""
File: BeeperCollectingKarel.py
--------------------------------
The BeeperCollectingKarel class collects all the beepers
in a series of vertical towers and deposits them at the
eastmost corner on 1st row.
"""
# import functions from other files.
from karel.stanfordkarel import *


def main():
    """
    This program collects all the beepers in a series of vertical towers.
    At the end, Karel will be facing East at the bottom row.
    And put all beepers that she has collected in the bag.
    """
    clear_all_towers()
    put_all_beepers()

# Clear all towers in Karel's world.'
# Move till front is clear and clear tower upward and downward.
# repeat until front is not clear.
def clear_all_towers():
    while front_is_clear():
        clear_tower_upward()
        move()
        clear_tower_downward()

# Put all beepers in Karel's bag. For this program, we assume that karel has not infinite number of beepers,
# there is enough space in Karel's bag to hold all the beepers.
def put_all_beepers():
    while beepers_in_bag():
        put_beeper()

# Turn till south is facing
# Move till wall is in front of Karel
# Turn till east is facing
def clear_tower_downward():
    face_south()
    move_and_pick()
    face_east()

# Turn till north is facing
# Move till wall is in front of Karel
# Turn till east is facing
def clear_tower_upward():
    face_north()
    move_and_pick()
    face_east()

# Move till front is clear and pick all beepers
def move_and_pick():
    while front_is_clear():
        while beepers_present():
            pick_beeper_safely()
        move()

# Pick beeper if present. It's a safety measure
def pick_beeper_safely():
    if beepers_present():
        pick_beeper()

# Turn till east is facing
def face_east():
    while not facing_east():
        turn_left()

# Turn till north is facing
def face_north():
    while not facing_north():
        turn_left()

# Turn till south is facing
def face_south():
    while not facing_south():
        turn_left()

if __name__ == "__main__":
    run_karel_program()
