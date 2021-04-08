import math

import pygame
from OpenGL.GL import *


class Image2D:
    def __init__(self, texture_path, camera, offsetFromCamera=None, attachedToCamera=False):
        self.texture_path = texture_path
        self.textureID = self.loadTexture()
        self.camera = camera
        self.attachedToCamera = attachedToCamera
        self.offsetFromCamera = offsetFromCamera

    def loadTexture(self):
        textureSurface = pygame.image.load(self.texture_path)
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()

        # glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        texid = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        return texid

    def draw(self):
        self.coordinates = self.calculateCoordinates(self.camera)

        # glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        glColor3f(1, 1, 1)
        glBindTexture(GL_TEXTURE_2D, self.textureID)

        glBegin(GL_QUADS)

        glTexCoord2f(0.0, 0.0)
        glVertex3f(self.coordinates[0][0], self.coordinates[0][1], self.coordinates[0][2])

        glTexCoord2f(1.0, 0.0)
        glVertex3f(self.coordinates[1][0], self.coordinates[1][1], self.coordinates[1][2])

        glTexCoord2f(1.0, 1.0)
        glVertex3f(self.coordinates[2][0], self.coordinates[2][1], self.coordinates[2][2])

        glTexCoord2f(0.0, 1.0)
        glVertex3f(self.coordinates[3][0], self.coordinates[3][1], self.coordinates[3][2])

        glEnd()

        glDisable(GL_TEXTURE_2D)
        glDisable(GL_BLEND)

    def calculateCoordinates(self, camera):
        pos = [camera.position[0], camera.position[1], camera.position[2]]
        yaw = camera.yaw

        distance = 2

        dx = math.sin(math.radians(yaw)) * distance
        dz = -math.cos(math.radians(yaw)) * distance

        pos[0] += dx
        pos[2] += dz

        yaw = 90 - yaw
        dx2 = math.sin(math.radians(yaw))
        dz2 = math.cos(math.radians(yaw))

        coords = [[-dx2, -2.0, -dz2], [dx2, -2.0, dz2], [dx2, -1.0, dz2], [-dx2, -1.0, -dz2]]

        coords = [[coords[0][0] + pos[0], coords[0][1] + pos[1], coords[0][2] + pos[2]],
                  [coords[1][0] + pos[0], coords[1][1] + pos[1], coords[1][2] + pos[2]],
                  [coords[2][0] + pos[0], coords[2][1] + pos[1], coords[2][2] + pos[2]],
                  [coords[3][0] + pos[0], coords[3][1] + pos[1], coords[3][2] + pos[2]]]

        xAverage = 0
        yAverage = 0
        zAverage = 0
        for coord in coords:
            xAverage += coord[0]
            yAverage += coord[1]
            zAverage += coord[2]
        xAverage /= len(coords)
        yAverage /= len(coords)
        zAverage /= len(coords)

        return coords
