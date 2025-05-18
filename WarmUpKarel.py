from karel.stanfordkarel import *

"""
File: WarmUpKarel.py
----------------------------
Write a program in the editor, that makes Karel move, pick a beeper, then move.
"""
def main():
    while not beepers_present():
        move()
    if beepers_present():
        pick_beeper()
        move()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
