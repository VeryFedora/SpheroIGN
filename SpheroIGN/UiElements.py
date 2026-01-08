from Sprite import Sprite
from CircleSprite import CircleSprite
import SpheroIGN
import pygame

# A simple reference class to hold values by reference.
class Reference:
    def __init__(self, val):
        self.value = val;

COLOR_BLUE = (0, 122, 255);
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


# These are the two circles that make the central navigation dial.
navigation_mover = CircleSprite(True, (1.0,1.0), COLOR_BLUE);
navigation_mover.clickCallback = navigation_mover_clicked;