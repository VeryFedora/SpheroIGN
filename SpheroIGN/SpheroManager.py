from spherov2.sphero_edu import SpheroEduAPI
from spherov2 import scanner
from SYSLIB import asyncio
from spherov2.types import Color

MAX_CONNECT_TRIES : int = 4

# Class that holds the sphero
class Robot:
    def init(self, mode):
        # Regular variables
        self.angle = 0;
        self.speed = 0;

        self.actual_robot = None;
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        for i in range(MAX_CONNECT_TRIES):
            try:
                self.robot = scanner.find_toy()
                self.actual_robot = SpheroEduAPI(self.robot)
                self.actual_robot.__enter__()  # start adapter/thread
                break
            except:
                print("failed to connect to device... retrying...")
        if(self.actual_robot):
            print("CONNECTED TO SPHERO: " + self.robot.toy_type.__str__() + self.robot.name)
        else:
            print("No robot found!")
            exit()
        print("Connected to Sphero RVR")
        if mode == "G":
            self.actual_robot.set_main_led(Color(r=255,g=0,b=0)) # Red for ghost.
        elif mode == "P":
            self.actual_robot.set_main_led(Color(r=255,g=255,b=0))
        self.actual_robot.set_heading(0)


    def setHeading(self, angle):
        print(abs(self.angle - angle))
        if(abs(self.angle - angle) > 1):
            self.actual_robot.set_heading(int(round(angle)))
            self.angle = int(round(angle))
            print(self.angle);

    def setSpeed(self, speed):
        if(abs(self.speed - speed) > 10):
            self.actual_robot.set_speed(int(round(speed)))
            self.speed = int(round(speed))
    

robot : Robot = None
           
def init():
    global robot
    robot = Robot()
    robot.init("P")
    
    # then initialize pygame / GUI
    

