import pygame
import pygame.image


class Scale:
    def __init__(self, x : int,y : int):
        self.x = x; 
        self.y = y;

class Sprite:
    sprite_list = []

    @staticmethod
    def renderSprites(screen):
        for sprite in Sprite.sprite_list:
            sprite.render(screen);

    def __init__(self, showing : bool, position : Scale, scale : Scale, color : tuple = None, texture : pygame.image = None):
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
            pygame.draw.rect(screen, self.rect, color=self.color);

    async def clicked(self):
        self.isClicked = True;
        if self.clickCallback != None:
            self.clickCallback();

    async def released(self):
        self.isClicked = False;
        if self.releaseCallback != None:
            self.releaseCallback();