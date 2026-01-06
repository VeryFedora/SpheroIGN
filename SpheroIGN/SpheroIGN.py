import pygame
import time 
import sys

import pygame.sprite
import SpheroManager
from Sprite import Sprite

def endProgram(msg:str):
    pygame.quit();
    print("Program exited with message: " + msg);
    sys.exit(0);

#### PROGRAM START #### 

pygame.init()
screen_dimensions = pygame.display.get_desktop_sizes();
screen = pygame.display.set_mode((screen_dimensions[0][0], screen_dimensions[0][1]));
pygame.display.set_caption("SpheroIGN");

BACKGROUND_COLOR : tuple = (255, 255, 255)
UPDATE_RATE : int = 30; # Updates per second

running : bool = True;
while(running):
    try:
        time.sleep(1/UPDATE_RATE);
        events = pygame.event.get();
        for event in events:
            # Break and quit.
            if event.type == pygame.QUIT:
                running = False;
                continue;
            # Handle mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos();
                for sprite in Sprite.sprite_list:
                    if sprite.rect.collidepoint(mouse_pos):
                        sprite.clicked();
            # Triggers once user releases the mouse.
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos();
                for sprite in Sprite.sprite_list:
                    if sprite.rect.collidepoint(mouse_pos):
                        sprite.released();
    except Exception:
        endProgram("An error occurred during the main loop: " + Exception.__str__());
        break;
    Sprite.renderSprites(Sprite.sprite_list, screen);
    screen.fill(BACKGROUND_COLOR);
    pygame.display.flip();
    
endProgram("Program Completed");
