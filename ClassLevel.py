import pygame
from Config import *
from ClassHero import Hero
from ClassBee import Bee
from ClassBackground import Background

class Level():
    def __init__(self, displaySurface):

        self.background = Background()

        self.hero = Hero((400, 400), faceRight=True)
        self.bee1 = Bee((200, 200), moveRight=True)
        self.bee2 = Bee((300, 300), moveRight=False)

        self.displaySurface = displaySurface

    def update(self):
        self.hero.update(self)
        self.bee1.update(self)
        self.bee2.update(self)

    def draw(self):
        self.background.draw(self.displaySurface)
        self.hero.draw(self.displaySurface)
        self.bee1.draw(self.displaySurface)
        self.bee2.draw(self.displaySurface)

    def run(self):
        self.update()
        self.draw()