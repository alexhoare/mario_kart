from OpenGL.GL import *
from OpenGL.GLU import *
import math
# import glm

class Camera(object):
    def __init__(self, position, yaw, pitch):
        self.position = position
        self.yaw = yaw
        self.pitch = pitch

        glRotatef(1, pitch, yaw, 0)
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])

    def move_forward(self, player, distance, maxVelocity):
        dx = -math.sin(math.radians(self.yaw)) * distance
        dz = math.cos(math.radians(self.yaw)) * distance

        player.acceleration = [dx, 0, dz]
        player.velocity = [player.velocity[0] + dx, player.velocity[1], player.velocity[2] + dz]
        totalVelocity = math.sqrt(player.velocity[0]**2 + player.velocity[2]**2)

        if totalVelocity > maxVelocity:
            dx = -math.sin(math.radians(self.yaw)) * maxVelocity
            dz = math.cos(math.radians(self.yaw)) * maxVelocity

            if (player.goingBackwards):
                player.velocity = [-dx, 0, -dz]
            else:
                player.velocity = [dx, 0, dz]


        #     player.acceleration = [0, 0, 0]
        #     biggerValue = max(player.velocity[0], player.velocity[2])
        #     print(biggerValue)
        #     if (biggerValue != 0):
        #         scaleFactor = maxVelocity / biggerValue
        #         player.velocity = [player.velocity[0] - dx, player.velocity[1], player.velocity[2] - dx]
            
        self.position = [self.position[0] - player.velocity[0], self.position[1], self.position[2] - player.velocity[2]]
        # print(self.position)
        glTranslatef(player.velocity[0], 0, player.velocity[2])

    def move(self, player, maxVelocity):
        # if math.sqrt(player.velocity[0]**2 + player.velocity[2]**2) > maxVelocity:
        #     player.acceleration = [0, 0, 0]
        #     biggerValue = max(player.velocity[0], player.velocity[2])
        #     if (biggerValue != 0):
        #         scaleFactor = maxVelocity / biggerValue
        #         player.velocity = [player.velocity[0] * scaleFactor, player.velocity[1] * scaleFactor, player.velocity[2] * scaleFactor]
        # else:
        player.velocity[0] += player.acceleration[0]
        player.velocity[2] += player.acceleration[2]

        self.position = [self.position[0] - player.velocity[0], self.position[1], self.position[2] - player.velocity[2]]
        glTranslatef(player.velocity[0], 0, player.velocity[2])
        
    def rotate(self, player, dyaw, dpitch, scaling_constant):
        self.yaw += dyaw * scaling_constant
        self.pitch += dpitch * scaling_constant
        self.yaw = self.yaw % 360
        self.pitch = self.pitch % 360

        dx = math.cos(math.radians(dyaw * scaling_constant)) * player.velocity[0] - math.sin(math.radians(dyaw * scaling_constant)) * player.velocity[2]
        dz = math.sin(math.radians(dyaw * scaling_constant)) * player.velocity[0] + math.cos(math.radians(dyaw * scaling_constant)) * player.velocity[2]
        # dx = -math.sin(math.radians(self.yaw)) * player.velocity[0]
        # dz = math.cos(math.radians(self.yaw)) * player.velocity[0]

        # player.acceleration = [dx, 0, dz]
        player.velocity = [dx, 0, dz]
        # player.velocity = [player.velocity[0] + dx, 0, player.velocity[1] + dz]
        # player.velocity = [player.velocity[0] + player.acceleration[0], player.velocity[1] + player.acceleration[1], player.velocity[2] + player.acceleration[2]]
        
        # (self.yaw, self.pitch)
        
        glTranslatef(self.position[0], self.position[1], self.position[2])
        
        glRotatef(scaling_constant, dpitch, dyaw, 0)
        
        glTranslatef(-self.position[0], -self.position[1], -self.position[2])
        
