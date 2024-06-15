import pygame
from Config import *
from ClassSpriteSheet import SpriteSheet

beeSprites = [
    (16,0,48,48),
    (80,0,48,48),
    (144,0,48,48),
    (208,0,48,48)
]

class Bee():

    def __init__(self, position, moveRight):
        self.flySpriteSheet = SpriteSheet(BEE_IMAGE, beeSprites)

        self.image = self.flySpriteSheet.getSprites(moveRight)[0]
        self.rect = self.image.get_rect(bottomleft = position)
        self.movingRight = moveRight
        self.animationIndex = 0
        self.currentState = 'FLY'

    def update(self, level):
        if self.movingRight == False:
            self.rect.x -= SPEED_BEE
        else:
            self.rect.x += SPEED_BEE

        if self.rect.right < 0:
            self.movingRight = True
        if self.rect.left > WINDOW_WIDTH:
            self.movingRight = False

        self.selectedAnimation()

        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0

        self.image = self.currentAnimation[int(self.animationIndex)]

    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)

    def selectedAnimation(self):
        self.animationSpeed = ANIMSPEED_BEE
        if self.currentState == 'FLY':
            self.currentAnimation = self.flySpriteSheet.getSprites(flipped = self.movingRight)

