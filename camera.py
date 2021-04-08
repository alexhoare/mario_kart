from OpenGL.GL import *
import math

class Camera(object):
    def __init__(self, position, yaw, pitch):
        self.position = position
        self.yaw = yaw
        self.pitch = pitch

        glRotatef(1, pitch, yaw, 0)
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])

    def move_forward(self, velocity):
        self.position = [self.position[0] - velocity[0], self.position[1], self.position[2] - velocity[2]]
        glTranslatef(velocity[0], 0, velocity[2])

    def move(self, velocity):
        self.position = [self.position[0] - velocity[0], self.position[1], self.position[2] - velocity[2]]
        glTranslatef(velocity[0], 0, velocity[2])
        
    def rotate(self, scaling_constant, dpitch, dyaw, droll):
        glTranslatef(self.position[0], self.position[1], self.position[2])

        glRotatef(scaling_constant, dpitch, dyaw, droll)

        glTranslatef(-self.position[0], -self.position[1], -self.position[2])

