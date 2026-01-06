import SpheroIGN
import time
import spherov2
from spherov2 import scanner

# Class that holds the sphero
class Unit:
    def __init__(self, mode):
        try:
            self.robot = scanner.find_toy()
            if(self.robot):
                self.robot.wake()
                self.robot.connect()
                print("Connected to Sphero RVR")
        except Exception as e:
            SpheroIGN.endProgram(str(e));

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

