import pygame
import math

class Game:
    def __init__(self, camera, player, track):
        self.camera = camera
        self.player = player
        self.track = track
        self.maxVelocity = 0.15

    def handleInput(self):
        pressed = pygame.key.get_pressed()
        
        self.player.turningLeft = False
        self.player.turningRight = False

        forward_constant = 0.01
        rotate_constant = 1
        if pressed[pygame.K_UP]:
            self.camera.move_forward(self.player, forward_constant, self.maxVelocity)
            self.player.goingBackwards = False
        else:
            self.camera.move_forward(self.player, 0, self.maxVelocity)
        if pressed[pygame.K_DOWN]:
            self.camera.move_forward(self.player, -forward_constant, self.maxVelocity)
            self.player.goingBackwards = True
        else:
            self.camera.move_forward(self.player, 0, self.maxVelocity)
        if pressed[pygame.K_LEFT]:
            self.player.turningLeft = True
            self.camera.rotate(self.player, -1, 0, rotate_constant)
        if pressed[pygame.K_RIGHT]:
            self.player.turningRight = True
            self.camera.rotate(self.player, 1, 0, rotate_constant)
        if pressed[pygame.K_j]:
            self.camera.rotate(self.player, 0, -1, rotate_constant)
        if pressed[pygame.K_k]:
            self.camera.rotate(self.player, 0, 1, rotate_constant)

    def gameLoop(self, display, displayDimensions):
        self.handleInput()
                
        self.track.draw()

        self.camera.move(self.player, self.maxVelocity)



        self.drawPlayer()

    def drawPlayer(self):
        pos = [self.camera.position[0], self.camera.position[1], self.camera.position[2]]
        yaw = self.camera.yaw

        distance = 2

        dx = math.sin(math.radians(yaw)) * distance
        dz = -math.cos(math.radians(yaw)) * distance
        dx1 = math.sin(math.radians(yaw)) * distance
        dz1 = -math.cos(math.radians(yaw)) * distance


        pos[0] += dx
        pos[2] += dz

        sinValue = -math.sin(math.radians(yaw))
        cosValue = math.cos(math.radians(yaw))


        yaw = 90-yaw
        dx2 = math.sin(math.radians(yaw))
        dz2 = math.cos(math.radians(yaw))

        coords = [[-dx2, -2.0, -dz2], [dx2, -2.0, dz2], [dx2, -1.0, dz2], [-dx2, -1.0, -dz2]]


        coords =   [[coords[0][0] + pos[0],  coords[0][1] + pos[1], coords[0][2] + pos[2]],
                    [coords[1][0] + pos[0],  coords[1][1] + pos[1], coords[1][2] + pos[2]],
                    [coords[2][0] + pos[0],  coords[2][1] + pos[1], coords[2][2] + pos[2]],
                    [coords[3][0] + pos[0],  coords[3][1] + pos[1], coords[3][2] + pos[2]]]

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

        diff = [pos[0] - xAverage, pos[1] - yAverage, pos[2] - zAverage]

        self.player.draw(coords)
