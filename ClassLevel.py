import pygame
from Config import *

class Level():
    def __init__(self, displaySurface):

        self.spyImage = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.spyImage = pygame.transform.scale(self.spyImage, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.displaySurface = displaySurface

    def update(self):
        pass

    def draw(self):
        self.displaySurface.blit(self.spyImage, (0, 0))

    def run(self):
        self.update()
        self.draw()