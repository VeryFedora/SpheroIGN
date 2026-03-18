from spherov2.sphero_edu import SpheroEduAPI
from spherov2 import scanner
from SYSLIB import asyncio
from spherov2.types import Color

# Class that holds the sphero
class Robot:
    def init(self, mode):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.robot = scanner.find_toy()
        with SpheroEduAPI(self.robot) as robot:
            if(self.robot):
                print("HOY")
            else:
                print("No robot found!")
                exit()
            print("Connected to Sphero RVR")
            if mode == "G":
                robot.set_main_led(color=[125, 0, 0])  # Red for ghost.
            elif mode == "P":
                robot.set_back_led(Color(r=0,g=255,b=0))

    def setHeading(self, angle):
        with SpheroEduAPI(self.robot) as robot:
            robot.set_heading(angle)

    def setSpeed(self, speed):
        with SpheroEduAPI(self.robot) as robot:
            robot.set_speed(speed)
    

robot : Robot = None
           
def init():
    global robot
    robot = Robot()
    robot.init("P")
    print("HEEEELLPPP")
    
    # then initialize pygame / GUI

