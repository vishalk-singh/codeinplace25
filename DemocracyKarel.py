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
