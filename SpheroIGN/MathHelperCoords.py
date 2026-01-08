import pygame
screen_dimensions = [(None, None)]
def fix_screen_dimensions(size):
    global screen_dimensions
    screen_dimensions = size
def getScreenSize():
    global screen_dimensions
    return screen_dimensions

class Scale:
    def __init__(self, x : int,y : int):
        self.x = x 
        self.y = y
class Coords:
    def __init__(self, x : int,y : int):
        self.x = x
        self.y = y