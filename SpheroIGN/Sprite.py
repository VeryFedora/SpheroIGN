import pygame
import pygame.image
sprite_list = []


class Scale:
    def __init__(self, x : int,y : int):
        self.x = x; 
        self.y = y;

class Sprite:

    @staticmethod
    def renderSprites(screen):
        for sprite in sprite_list:
            sprite.render(screen);

    def __init__(self, showing : bool, position : Scale, scale : Scale, color : tuple = None, texture : pygame.image = None):
        # Position in rendering list
        self.ID = len(sprite_list);
        # Rendering properties
        self.showing = showing;
        self.position = position
        self.scale = scale
        self.color = color;
        self.texture = texture;
        self.rect = pygame.rect.Rect(self.position.x, self.position.y, self.scale.x, self.scale.y);
        sprite_list.append(self);
        # Input and output
        self.clickCallback = None;
        self.isClicked = False;

    def render(self, screen):
        if self.showing:
            pygame.draw.rect(screen, self.rect);

    def move(self, x, y):
        self.position.x += x;
        self.position.y += y;

    async def clicked(self):
        self.isClicked = True;
        if self.clickCallback != None:
            self.clickCallback();

    async def released(self):
        self.isClicked = False;
    