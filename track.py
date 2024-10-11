import pygame
from OpenGL.GL import *
from PIL import Image


class Track:
    def __init__(self, texture_path, coordinates, camera):
        self.texture_path = texture_path
        self.coordinates = coordinates
        self.camera = camera
        self.textureID = self.loadTexture()
        self.trackWidth = abs(coordinates[2][0] - coordinates[0][0])
        self.trackHeight = abs(coordinates[2][2] - coordinates[0][2])
        self.image = Image.open("assets/accelerationMap.png").convert("RGB")
        self.imageWidth, self.imageHeight = self.image.size;


    def loadTexture(self):
        textureSurface = pygame.image.load(self.texture_path)
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()

        glEnable(GL_TEXTURE_2D)
        texid = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        return texid

    def draw(self):
        glEnable(GL_TEXTURE_2D)
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

    def positionToPixel(self, x, z):
        pixels = self.image.load()

        widthScale = self.imageWidth / self.trackWidth
        heightScale = self.imageHeight / self.trackHeight
        row = (x + (self.trackWidth / 2)) * heightScale
        column = (z + (self.trackHeight / 2)) * widthScale

        color = pixels[row, column]

        return color

    def colorToDeceleration(self, color):
        if color[0] > 200 and color[1] < 200 and color[2] < 200:
            return 0
        if color[2] > 200 and color[0] < 200 and color[1] < 200:
            return 0.95
        return 0.99