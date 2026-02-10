from copy import deepcopy
from Sprite import Sprite
from CircleSprite import CircleSprite
from MathHelperCoords import Coords, Scale, Reference
import pygame
from ButtonClass import Button
import GlobalLoopVariables

# A simple reference class to hold values by reference.
class Reference:
    def __init__(self, val):
        self.value = val;

# Color constants
COLOR_BLUE = (0, 122, 255);
COLOR_BLACK = (25, 25, 25);
COLOR_RED = (200, 0, 0);
COLOR_DARK_GREY = (100, 100, 100);
COLOR_GREY = (200,200,200);
COLOR_GREEN = (0, 200, 100);
COLOR_PURPLE = (200, 150, 220);

# CONSTANTS FOR UI ELEMENTS
NAVIGATION_CONTAINER_RADIUS = 200;
NAVIGATION_MOVER_RADIUS = 40;
NAVIGATION_BORDER_SIZE = 10;
NAVIGATION_POSITION = pygame.Vector2(1350, 700);
TOP_BAR_Y = 0;


# fires when the navigation mover is clicked
#@staticmethod

# This function is added to global callback list.
def navigation_mover_held(button : Button):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    direction = mouse_pos - NAVIGATION_POSITION
    if direction.length() > NAVIGATION_CONTAINER_RADIUS-NAVIGATION_MOVER_RADIUS:
        direction.scale_to_length(NAVIGATION_CONTAINER_RADIUS-NAVIGATION_MOVER_RADIUS)

    button.boundSprite.position = NAVIGATION_POSITION + direction

def navigation_mover_clicked(button : Button):
    # Loop until released, stillclicked should be a boolean.
    button.heldCallbackID = len(GlobalLoopVariables.loop_callback_list.get());
    GlobalLoopVariables.loop_callback_list.value.append(lambda: navigation_mover_held(button));
    return;

def navigation_mover_released(button : Button):
    # Remove the held callback from the global loop callback list.
    if button.heldCallbackID != -1:
        GlobalLoopVariables.loop_callback_list.value.pop(button.heldCallbackID);
        button.heldCallbackID = -1;
        button.boundSprite.position = NAVIGATION_POSITION;

def quit_button_pressed(button : Button):
    pygame.quit()
    exit()

def initElements():
    # These are the three circles that make the central navigation dial.
    global navigation_border # Black border around it all
    navigation_border = CircleSprite(True, deepcopy(NAVIGATION_POSITION), NAVIGATION_CONTAINER_RADIUS + NAVIGATION_BORDER_SIZE, COLOR_BLACK);
    global navigation_holder # Circle that contains the navigation mover
    navigation_holder = CircleSprite(True, deepcopy(NAVIGATION_POSITION), NAVIGATION_CONTAINER_RADIUS, COLOR_GREY)
    global navigation_mover # Circle that the player actually controls
    navigation_mover = CircleSprite(True, deepcopy(NAVIGATION_POSITION), NAVIGATION_MOVER_RADIUS, COLOR_BLUE)
    navigation_mover_button = Button(navigation_mover_clicked);
    navigation_mover_button.releaseCallback = navigation_mover_released;
    navigation_mover_button.bindSprite(navigation_mover);
    #navigation_mover.clickCallback = navigation_mover_clicked
    # Top bar
    global top_bar
    top_bar = Sprite(True, Coords(0,TOP_BAR_Y), Scale(3000,100), COLOR_BLUE, None);
    # Quit button on top bar
    global quit_button
    quit_button_sprite = Sprite(True, Coords(1580,TOP_BAR_Y), Scale(130,100), COLOR_RED, None);
    quit_button = Button(quit_button_pressed);
    quit_button.bindSprite(quit_button_sprite);
    # settings button
    global settings_button
    settings_button = Sprite(True, Coords(775, TOP_BAR_Y), Scale(150,100), COLOR_DARK_GREY, None);
    # Home page button
    global home_button
    home_button = Sprite(True, Coords(0, TOP_BAR_Y), Scale(130,100), COLOR_GREEN, None);

    ## Decoration for home page ##
    global circle_decor
    circle_decor = CircleSprite(True, Coords(400, 400), 100, COLOR_PURPLE);
   
def change_theme_to_red():
    global navigation_border;
    navigation_border.color = COLOR_RED;
    global navigation_holder;
    navigation_holder.color = COLOR_DARK_GREY;
    global naigation_mover;
    navigation_mover.color = COLOR_RED;
    global top_bar;
    top_bar.color = COLOR_RED;

change_theme_to_red();
