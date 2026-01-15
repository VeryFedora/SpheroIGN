import pygame
from Sprite import Sprite
from CircleSprite import CircleSprite

from MathHelperCoords import Reference
class Button:
    button_list = []

    @staticmethod
    def renderButtons(screen):
        for button in Button.button_list:
            button.render(screen);

    def __init__(self, callback, releaseCallback = None):
        self.ID = len(Button.button_list);
        Button.button_list.append(self);
        self.clickCallback = callback;
        self.releaseCallback = releaseCallback;
        self.isClicked : Reference = Reference(False);
        self.boundSprite = None;
        # Index of the callback in the global loop callback list, if present.
        self.heldCallbackID = -1;
        
     
    def bindSprite(self, sprite):
        self.boundSprite = sprite;

    def checkCollision(self):
        if self.boundSprite:
            if type(self.boundSprite) == Sprite:
                return self.boundSprite.rect.collidepoint(pygame.mouse.get_pos())
            elif type(self.boundSprite) == CircleSprite:
                dist_x = self.boundSprite.position.x - pygame.mouse.get_pos()[0]
                dist_y = self.boundSprite.position.y - pygame.mouse.get_pos()[1]
                distance = (dist_x ** 2 + dist_y ** 2) ** 0.5
                return distance <= self.boundSprite.scale
        

    def clicked(self, mouseDown : Reference):
        self.isClicked = mouseDown;
        if self.clickCallback != None:
            self.clickCallback(self, mouseDown);

    def released(self):
        self.isClicked.value = False;
        if self.releaseCallback != None:
            self.releaseCallback(self);

