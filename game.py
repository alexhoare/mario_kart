import pygame


class Game:
    def __init__(self, camera, player, track):
        self.camera = camera
        self.player = player
        self.track = track
        self.maxVelocity = 0.15
        self.trackDeceleration = 1.0

    def handleInput(self):
        pressed = pygame.key.get_pressed()

        self.player.turningLeft = False
        self.player.turningRight = False

        forward_constant = 0.01
        rotate_constant = 1
        if pressed[pygame.K_UP]:
            self.player.move_forward(forward_constant, self.maxVelocity, self.trackDeceleration)
            self.player.goingBackwards = False
        else:
            self.player.move_forward(0, self.maxVelocity, self.trackDeceleration)
        if pressed[pygame.K_DOWN]:
            self.player.move_forward(-forward_constant, self.maxVelocity, self.trackDeceleration)
            self.player.goingBackwards = True
        else:
            self.player.move_forward(0, self.maxVelocity, self.trackDeceleration)
        if pressed[pygame.K_LEFT]:
            self.player.turningLeft = True
            self.player.rotate(rotate_constant, 0, -1)
        if pressed[pygame.K_RIGHT]:
            self.player.turningRight = True
            self.player.rotate(rotate_constant, 0, 1)
        if pressed[pygame.K_j]:
            self.player.rotate(rotate_constant, -1, 0)
        if pressed[pygame.K_k]:
            self.player.rotate(rotate_constant, 1, 0)


    def gameLoop(self):
        self.handleInput()

        self.track.draw()

        self.player.move(self.maxVelocity, self.trackDeceleration)

        self.drawPlayer()


        x = self.camera.position[0]
        z = self.camera.position[2]
        # x = self.camera.position[0] + self.player.velocity[0] * 2
        # z = self.camera.position[2] + self.player.velocity[2] * 2
        # if (self.player.goingBackwards):
        #     x = -x
        #     z = -z

        color = self.track.positionToPixel(x, z)
        self.trackDeceleration = self.track.colorToDeceleration(color)
        # print(self.trackDeceleration)

    def drawPlayer(self):
        self.player.draw(self.camera)
