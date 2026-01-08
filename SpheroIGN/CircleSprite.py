import pygame
import Sprite

class CircleSprite:
    sprite_list = []

    @staticmethod
    def renderSprites(screen):
        for sprite in CircleSprite.sprite_list:
            sprite.render(screen);

    def __init__(self, showing : bool,position : Sprite.Scale,  scale : Sprite.Scale, color : tuple = None):
        self.ID = len(CircleSprite.sprite_list);
        self.showing = showing;
        self.position = position;
        self.scale = scale;
        self.color = color;
        CircleSprite.sprite_list.append(self);
        self.clickCallback = None;
        self.isClicked = False;

    def render(self, screen):
        if self.showing:
            pygame.draw.circle(screen, self.color, (self.position.x+self.scale.x // 2, self.position.y + self.scale.y // 2), min(self.scale.x,self.scale.y)//2);

    async def clicked(self):
        self.isClicked = True;
        if self.clickCallback != None:
            self.clickCallback();

    async def released(self):
        self.isClicked = False;
        if self.releaseCallback != None:
            self.releaseCallback();