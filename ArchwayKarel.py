from karel.stanfordkarel import *

"""
File: ArchwayKarel.py
----------------------------
Karel will be in a world with an archway 
Write a program which will move Karel up and over the archway,
so Karel ends up on the right side of it facing East.
1. Karel should turn north(left) and move up until it hits the archway.
2. karel should turn right and move forward until it hits the top of the archway.
3. karel should turn right and move forward until it hits the bottom of the archway.
4. Karel should end up facing East.
"""
def main():
    # Turn till north is facing and move till wall is in front of Karel.
    # Turn till east is facing and move till wall is in front of Karel.
    # Turn till south is facing and move till wall is in front of Karel and at the bottom of the archway.
    # Turn till east is facing and move till wall is in front of Karel.
    climb_archway()
    move_to_wall()
    descend_archway()
# Turn till north is facing
# Move till wall is in front of Karel
# Turn till east is facing
def climb_archway():
    face_north()
    move_to_wall()
    face_east()

# Turn till south is facing
# Move till wall is in front of Karel
# Turn till east is facing
def descend_archway():
    face_south()
    move_to_wall()
    face_east()

# Turn till south is facing
def face_south():
    while not facing_south():
        turn_left()

# Move till wall is in front of Karel
def move_to_wall():
    while front_is_clear():
        move()

# turn till east is facing
def face_east():
    while not facing_east():
        turn_left()

# turn till north is facing
def face_north():
    while not facing_north():
        turn_left()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
