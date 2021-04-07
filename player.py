import math

from OpenGL.GL import *

from image2d import Image2D


class Player(object):
    def __init__(self, velocity, acceleration):
        self.acceleration = acceleration
        self.velocity = velocity
        # self.image = Image2D('player.png', [[]], camera)
        self.turningRight = False
        self.turningLeft = False
        self.goingBackwards = False

    def draw(self, camera):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if self.turningRight and not self.turningLeft:
            self.image = Image2D('assets/turnRight.png', camera)
        elif self.turningLeft and not self.turningRight:
            self.image = Image2D('assets/turnLeft.png', camera)
        else:
            self.image = Image2D('assets/player.png', camera)

        self.image.draw()



