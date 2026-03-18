import sys
sys.coinit_flags = 0
import pygame
import time 
import MathHelperCoords
from MathHelperCoords import Reference
import SpheroManager
import UiElements
import ButtonClass
import GlobalLoopVariables
from Sprite import Sprite
from CircleSprite import CircleSprite


#### PROGRAM START #### 
running : bool = True;
# Discerning mouse properties
mouse_pos : tuple = (0,0);
mouse_down : Reference = Reference(False);
bound_button : ButtonClass.Button = None;
def run():
    SpheroManager.init()
    pygame.init()
    MathHelperCoords.fix_screen_dimensions(pygame.display.get_desktop_sizes());
    print(str(MathHelperCoords.getScreenSize()));
    screen = pygame.display.set_mode((MathHelperCoords.getScreenSize()[0][0], MathHelperCoords.getScreenSize()[0][1]));
    pygame.display.set_caption("SpheroIGN");

    UiElements.initElements();
    Sprite.init_all();
    BACKGROUND_COLOR : tuple = (255, 255, 255)
    UPDATE_RATE : int = 30; # Updates per second
    global running
    global mouse_pos
    global mouse_down 
    global bound_button
    
    while(running): 
        mouse_pos = pygame.mouse.get_pos();
        pygame.display.flip();
        time.sleep(1/UPDATE_RATE);
        events = pygame.event.get();
        for event in events:
            # Break and quit.
            if event.type == pygame.QUIT:
                running = False;
                continue;
            # Handle mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in ButtonClass.Button.button_list:
                    if(button.checkCollision()):
                        bound_button = button;
                        button.clicked();
                        break;
            # Triggers once user releases the mouse.
            elif event.type == pygame.MOUSEBUTTONUP:
                if bound_button:
                    bound_button.released();
                    bound_button = None;
                    mouse_down.value = False;
        # Call global loop callbacks, if any. This goes through all events requested by other sections.
        for loop_callback in GlobalLoopVariables.loop_callback_list.get():
            loop_callback();
        screen.fill(BACKGROUND_COLOR);
        Sprite.renderSprites(screen);
        CircleSprite.renderSprites(screen);
    
run();