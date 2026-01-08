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

    def __init__(self):
        self.ID = len(Button.button_list);
        Button.button_list.append(self);
        self.clickCallback = None;
        self.isClicked : Reference = Reference(False);
        self.boundSprite = None;
     
    def bindSprite(self, sprite):
        self.boundSprite = sprite;

    def checkCollision():
        if self.sprite:
            if type(self.sprite) == Sprite:
                return self.sprite.rect.collidepoint(pygame.mouse.get_pos())
            elif type(self.sprite) == CircleSprite:
                dist_x = self.sprite.position.x - pygame.mouse.get_pos()[0];
                dist_y = self.sprite.position.y - pygame.mouse.get_pos()[1];
                distance = (dist_x ** 2 + dist_y ** 2) ** 0.5;
                return distance <= self.sprite.scale;
        

    async def clicked(self):
        self.isClicked = True;
        if self.clickCallback != None:
            self.clickCallback();

    async def released(self):
        self.isClicked = False;
        if self.releaseCallback != None:
            self.releaseCallback();

