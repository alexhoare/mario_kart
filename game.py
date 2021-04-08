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
            self.player.move_forward(forward_constant, self.maxVelocity)
            self.player.goingBackwards = False
        else:
            self.player.move_forward(0, self.maxVelocity)
        if pressed[pygame.K_DOWN]:
            self.player.move_forward(-forward_constant, self.maxVelocity)
            self.player.goingBackwards = True
        else:
            self.player.move_forward(0, self.maxVelocity)
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

        self.player.move(self.maxVelocity)

        self.drawPlayer()


        x = self.camera.position[0]
        z = self.camera.position[2]
        color = self.track.positionToPixel(x, z)
        print(color)

    def drawPlayer(self):
        self.player.draw(self.camera)
