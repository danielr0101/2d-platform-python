import pygame
from Config import *

class Background():
    def __init__(self):
        
        self.spyImage = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.spyImage = pygame.transform.scale(self.spyImage, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def draw(self, displaySurface):
        displaySurface.blit(self.spyImage, (0, 0))