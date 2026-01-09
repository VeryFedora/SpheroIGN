from Sprite import Sprite
from CircleSprite import CircleSprite
from MathHelperCoords import Coords, Scale, Reference
import pygame
from ButtonClass import Button

# A simple reference class to hold values by reference.
class Reference:
    def __init__(self, val):
        self.value = val;

COLOR_BLUE = (0, 122, 255);
COLOR_BLACK = (25, 25, 25);
COLOR_RED = (200, 0, 0);
COLOR_DARK_GREY = (100, 100, 100);
COLOR_GREY = (200,200,200);
COLOR_GREEN = (0, 200, 100);
COLOR_PURPLE = (50, 50, 150);

# fires when the navigation mover is clicked
@staticmethod
async def navigation_mover_clicked(stillclicked : Reference, item : CircleSprite, return_x : int, return_y : int):
    # Loop until released, stillclicked should be a boolean.
    while stillclicked.value:
        item.position.x = pygame.mouse.get_pos()[0] - item.scale.x // 2;
        item.position.y = pygame.mouse.get_pos()[1] - item.scale.y // 2;
    item.position.x = return_x;
    item.position.y = return_y;
    return;

# CONSTANTS FOR UI ELEMENTS
NAVIGATION_CONTAINER_RADIUS = 200;
NAVIGATION_MOVER_RADIUS = 40;
NAVIGATION_BORDER_SIZE = 10;
NAVIGATION_POSITION = Coords(1350, 700);
TOP_BAR_Y = 0;

# fires when the navigation mover is clicked
@staticmethod
async def navigation_mover_clicked(button, stillclicked : Reference):
    global NAVIGATION_POSITION
    # Loop until released, stillclicked should be a boolean.
    while stillclicked.value:
        button.sprite.position.x = pygame.mouse.get_pos()[0] - button.sprite.scale.x // 2;
        button.sprite.position.y = pygame.mouse.get_pos()[1] - button.sprite.scale.y // 2;
        button.sprite.position.x = NAVIGATION_POSITION.x;
        button.sprite.position.y = NAVIGATION_POSITION.y;
        return;


def initElements():
    # These are the three circles that make the central navigation dial.
    global navigation_border # Black border around it all
    navigation_border = CircleSprite(True, NAVIGATION_POSITION, NAVIGATION_CONTAINER_RADIUS + NAVIGATION_BORDER_SIZE, COLOR_BLACK);
    global navigation_holder # Circle that contains the navigation mover
    navigation_holder = CircleSprite(True, NAVIGATION_POSITION, NAVIGATION_CONTAINER_RADIUS, COLOR_GREY)
    global navigation_mover # Circle that the player actually controls
    navigation_mover = CircleSprite(True, NAVIGATION_POSITION, NAVIGATION_MOVER_RADIUS, COLOR_BLUE)
    #navigation_mover.clickCallback = navigation_mover_clicked
    # Top bar
    global top_bar
    top_bar = Sprite(True, Coords(0,TOP_BAR_Y), Scale(3000,100), COLOR_BLUE, None);
    # Quit button on top bar
    global quit_button
    quit_button = Sprite(True, Coords(1590,TOP_BAR_Y + 100), Scale(120,100), COLOR_RED, None);
    # settings button
    global settings_button
    settings_button = Sprite(True, Coords(770, TOP_BAR_Y + 100), Scale(150,100), COLOR_DARK_GREY, None);
    # Home page button
    global home_button
    home_button = Sprite(True, Coords(0, TOP_BAR_Y + 100), Scale(130,100), COLOR_GREEN, None);

    ## Decoration for home page ##
    global circle_decor
    circle_decor = CircleSprite(True, Coords(400, 400), 300, COLOR_PURPLE);
    top_bar = Sprite(True, Coords(0,TOP_BAR_Y), Scale(3000,50), COLOR_BLUE, None);



