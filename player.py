import math

from OpenGL.GL import *

from image2d import Image2D


class Player(object):
    def __init__(self, velocity, acceleration, camera):
        self.acceleration = acceleration
        self.velocity = velocity
        # self.image = Image2D('player.png', [[]], camera)
        self.turningRight = False
        self.turningLeft = False
        self.goingBackwards = False

        self.camera = camera

    def draw(self, camera):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        if self.turningRight and not self.turningLeft:
            self.image = Image2D('assets/turnRight.png', camera)
        elif self.turningLeft and not self.turningRight:
            self.image = Image2D('assets/turnLeft.png', camera)
        else:
            self.image = Image2D('assets/player.png', camera)

        self.image.draw()

    def printPosition(self):
        print(self.camera.position[0], self.camera.position[1], self.camera.position[2])

    def move_forward(self, distance, maxVelocity, trackDeceleration):
        ddx = -math.sin(math.radians(self.camera.yaw)) * distance
        ddz = math.cos(math.radians(self.camera.yaw)) * distance

        if trackDeceleration == 0:
            # self.velocity = [-ddx, 0, -ddz]
            if (self.velocity == [0, 0, 0]):
                self.velocity = [ddx, 0, ddz]
            else:
                self.velocity = [0, 0, 0]

        #     self.acceleration = [0, 0, 0]
            self.camera.move_forward(self.velocity)
            return

        self.acceleration = [ddx, 0, ddz]
        self.velocity = [trackDeceleration * (self.velocity[0] + ddx), trackDeceleration * (self.velocity[1]), trackDeceleration * (self.velocity[2] + ddz)]

        totalVelocity = math.sqrt(self.velocity[0]**2 + self.velocity[2]**2)

        if totalVelocity > maxVelocity:
            dx = -math.sin(math.radians(self.camera.yaw)) * maxVelocity * trackDeceleration
            dz = math.cos(math.radians(self.camera.yaw)) * maxVelocity * trackDeceleration

            if (self.goingBackwards):
                self.velocity = [-dx, 0, -dz]
            else:
                self.velocity = [dx, 0, dz]


        self.camera.move_forward(self.velocity)


    def move(self, maxVelocity, trackDeceleration):
        self.velocity[0] += self.acceleration[0]
        self.velocity[2] += self.acceleration[2]

        self.camera.move(self.velocity)

    def rotate(self, scaling_constant, dpitch, dyaw):
        self.camera.yaw += dyaw * scaling_constant
        self.camera.pitch += dpitch * scaling_constant
        self.camera.yaw = self.camera.yaw % 360
        self.camera.pitch = self.camera.pitch % 360

        dx = math.cos(math.radians(dyaw * scaling_constant)) * self.velocity[0] - math.sin(
            math.radians(dyaw * scaling_constant)) * self.velocity[2]
        dz = math.sin(math.radians(dyaw * scaling_constant)) * self.velocity[0] + math.cos(
            math.radians(dyaw * scaling_constant)) * self.velocity[2]

        self.velocity = [dx, 0, dz]

        self.camera.rotate(scaling_constant, dpitch, dyaw, 0)