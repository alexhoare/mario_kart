import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from image2d import Image2D

class Player(object):
    def __init__(self, velocity, acceleration):
        self.acceleration = acceleration
        self.velocity = velocity
        self.image = Image2D('player.png', [[]])
        self.turningRight = False
        self.turningLeft = False
        self.goingBackwards = False

    def draw(self, coords):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if self.turningRight and not self.turningLeft:
            self.image = Image2D('turnRight.png', coords)
        elif self.turningLeft and not self.turningRight:
            self.image = Image2D('turnLeft.png', coords)
        else:
            self.image = Image2D('player.png', coords)

        self.image.draw()
