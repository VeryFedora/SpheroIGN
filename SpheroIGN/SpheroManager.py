import SpheroIGN
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI


# Class that holds the sphero
class Robot:
    def __init__(self, mode):
        try:
            self.robot = scanner.find_toy()
            if(self.robot):
                self.robot.wake()
                self.robot.connect()
                print("Connected to Sphero RVR")
            if mode == "G":
                self.robot.set_main_led(color=[125, 0, 0])  # Red for ghost.
            elif mode == "P":
                self.robot.set_main_led(color=[0,125,125]) # Teal for player
        except Exception as e:
            SpheroIGN.endProgram(str(e));

    def setHeading(self, angle):
        with SpheroEduAPI(self.robot) as robot:
            robot.set_heading(angle)

    def setSpeed(self, speed):
        with SpheroEduAPI(self.robot) as robot:
            robot.set_speed(speed)
    

robot : Robot
           
def init():
    global robot
    robot = Robot()
    

