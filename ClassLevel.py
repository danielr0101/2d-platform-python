import pygame
from Config import *
from ClassBackground import Background

class Level():
    def __init__(self, displaySurface):

        self.background = Background()

        self.displaySurface = displaySurface

    def update(self):
        pass

    def draw(self):
        self.background.draw(self.displaySurface)

    def run(self):
        self.update()
        self.draw()