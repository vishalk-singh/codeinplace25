"""
File: BeeperCollectingKarel.py
--------------------------------
The BeeperCollectingKarel class collects all the beepers
in a series of vertical towers and deposits them at the
eastmost corner on 1st row.
"""
from karel.stanfordkarel import *


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
