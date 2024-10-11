import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image
from PIL import ImageOps


from camera import Camera
from image2d import Image2D
from player import Player
from game import Game
from track import Track


def main():
    pygame.init()
    displayDimensions = (1280, 720)
    
    display = pygame.display.set_mode(displayDimensions, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, displayDimensions[0]/displayDimensions[1], 0.1, 500)

    camera = Camera([-140, 2, 10], 0, 0)

    player = Player([0, 0, 0], [0, 0, 0], camera)
    player.rotate(20, 1, 0)

    trackCoordinates = [[-200.0, -1.0, 200.0], [200.0, -1.0, 200.0], [200.0, -1.0, -200.0], [-200.0, -1.0, -200.0]]
    track = Track('assets/track.png', trackCoordinates, camera)

    game = Game(camera, player, track)

    while True:
        for event in pygame.event.get():
            # quit if app is closed or "q" is pressed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                quit()

        # clear the screen
        glColorMask(True, True, True, True)
        glClearColor(0.53, 0.81, 0.92, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        game.gameLoop()

        # update the screen
        pygame.display.flip()

        pygame.time.wait(10)
main()
