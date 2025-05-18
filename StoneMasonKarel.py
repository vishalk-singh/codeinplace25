from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
1. StoneMasonKarel should solve the "repair the quad". 
2. program works for all of the sample worlds supplied in the starter folder.
3. Building one pillar at a time. start from the bottom. Use while loop front_is_clear() to build pillar.
4. Turn left at the end of each pillar and move back to the bottom.
5. Put beepers at the end of each pillar if there is no beeper at the end of the pillar to solve fence post problem.
6. Move to the next pillar.
7. Repeat until all pillars are built.
8. Repeat process for the last pillar out side of while loop due to fence post problem.
"""


def main():
    make_stone_mason()

def make_stone_mason():
    while front_is_clear():
        build_pillar()
        move_to_bottom()
        move_to_next_pillar()
    build_pillar()
    move_to_bottom()

def move_to_bottom():
    turn_right()
    move_to_next_pillar()
    turn_left()

def move_to_next_pillar():
    for i in range(4):
        if front_is_clear():
            move()

def build_pillar():
    turn_left()
    build_pile()
    turn_right()

def build_pile():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
    if not beepers_present():
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
