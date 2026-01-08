import pygame
import pygame.image

class ButtonClass:
    button_list = []
    @staticmethod
    def renderButtons(screen):
        for button in ButtonClass.button_list:
            button.render(screen);

    def __init__(self, showing : bool, position : tuple, scale : tuple, color : tuple = None, texture : pygame.image = None):
        self.ID = len(ButtonClass.button_list);
        self.showing = showing;
        ButtonClass.button_list.append(self);
        self.clickCallback = None;
        self.isClicked = False;

    async def clicked(self):
        self.isClicked = True;
        if self.clickCallback != None:
            self.clickCallback();

    async def released(self):
        self.isClicked = False;
        if self.releaseCallback != None:
            self.releaseCallback();
