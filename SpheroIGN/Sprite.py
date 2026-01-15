import pygame
import pygame.image
from MathHelperCoords import Coords, Scale, getScreenSize

class Sprite:
    sprite_list = []

    @staticmethod
    def renderSprites(screen):
        for sprite in Sprite.sprite_list:
            sprite.render(screen);
    @staticmethod
    def init_all():
        print(str(getScreenSize()))
        for sprite in Sprite.sprite_list:
            sprite.position = Coords(int(sprite.position.x / float(480/getScreenSize()[0][0])), int(sprite.position.y / float(480/getScreenSize()[0][1])));
            sprite.scale = Coords(int(sprite.position.x / float(480/getScreenSize()[0][0])), int(sprite.position.y / float(480/getScreenSize()[0][1])));

    def __init__(self, showing : bool, position : Coords, scale : Scale, color : tuple = None, texture : pygame.image = None):
        # Position in rendering list
        self.ID = len(Sprite.sprite_list);
        # Rendering properties
        self.showing = showing;
        self.position = position;
        self.scale = scale;              
        self.color = color;
        self.texture = texture;
        self.rect = pygame.rect.Rect(position.x, position.y, self.scale.x, self.scale.y);
        Sprite.sprite_list.append(self);
        # Input and output
        self.clickCallback = None;
        self.releaseCallback = None;
        self.isClicked = False;


    def move(self, x, y):
        self.rect.move(x, y);

    def render(self, screen):
        if self.showing:
            pygame.draw.rect(screen, rect = self.rect, color=self.color);