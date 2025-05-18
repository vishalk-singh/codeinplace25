from karel.stanfordkarel import *
"""
File: HospitalKarel.py
------------------------
Run the blank programme. 
Each beeper in the represents a pile of supplies. 
Karel's job is to walk along 1st Street and build a new hospital in the places marked by each beeper. 
The new hospital should be centered at the point at which the bit of debris was left, 
which means that the first hospital in the diagram above will be constructed with its left edge along 2nd Avenue, 
since the beeper was originally at 3rd Avenue.
At the end of the run, Karel should be at the east end of 1st street facing East.

Keep in mind the following information about the world:
1. Karel starts facing east at (1, 1) with an infinite number of beepers in its beeper bag.
2. The beepers indicating the positions at which hospitals should be built will be spaced so that 
    there is room to build the hospitals without overlapping or hitting walls.
3. You will not have to build a hospital that starts in either of the last two columns.
4. Karel should not crash into a wall if it builds a hospital that ends in the final corner.

Write the code to implement Hospital Karel. 
Use helper functions. Think, "what are the high-level steps Karel needs to take?" 
and make these steps into helper functions. 
Remember that your program should work for any world that meets the above conditions.
"""


def main():
    pass

def turn_right():
   for i in range(3):
      turn_left()

def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
