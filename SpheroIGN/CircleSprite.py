import pygame
from MathHelperCoords import Coords

class CircleSprite:
    sprite_list = []
    
    @staticmethod
    def renderSprites(screen):
        for sprite in CircleSprite.sprite_list:
            sprite.render(screen);

    def __init__(self, showing : bool,position : Coords,  scale : int, color : tuple = None):
        self.ID = len(CircleSprite.sprite_list);
        self.showing = showing;
        self.position = position;
        self.scale = scale;
        self.color = color;
        CircleSprite.sprite_list.append(self);

    def render(self, screen):
        if self.showing:
            pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.scale);