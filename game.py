import pygame


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


    def gameLoop(self):
        self.handleInput()

        self.track.draw()

        self.camera.move(self.player, self.maxVelocity)

        self.drawPlayer()

    def drawPlayer(self):
        self.player.draw(self.camera)
