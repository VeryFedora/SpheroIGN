import spherov2
import pygame

def endProgram(msg:str):
        print("Program exited with message: " + msg)
        exit(0);
# Class that holds the sphero
class Unit:
    def __init__(self):
        self.robot = spherov2.Sphero()
        try:
            self.robot.wake()
            self.robot.connect()
            print("Connected to Sphero RVR")
        except Exception as e:
            endProgram("Failed to connect to Sphero RVR: " + str(e))

# Declare globals
player : Unit
# Enemies
subroutine_alpha : Unit
subroutine_beta : Unit
subroutine_charlie : Unit
subroutine_delta : Unit
def init():
    player = Unit()

    subroutine_alpha = Unit()
    subroutine_beta = Unit()
    subroutine_charlie = Unit()
    subroutine_delta = Unit()

    endProgram("Program exited.")