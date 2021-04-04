import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL import Image
from PIL import ImageOps

# uncomment if on school computer
# import os
# os.chdir("C:/Users/ahoare2/Downloads/Programming/Semester Project")

from camera import Camera
# from track import Track
from image2d import Image2D
from player import Player
from game import Game
from track import Track

vertices = (
        (1, 1, -1),
        (1, -1, -1),
        (-1, -1, -1),
        (-1, 1, -1),        
        (1, 1, 1),
        (1, -1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )
        
edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
        )


def Cube(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for index in edge:
            glVertex3fv(vertices[index])
    glEnd()
    


def main():
    pygame.init()
    displayDimensions = (1920, 1080)
    
    display = pygame.display.set_mode(displayDimensions, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, displayDimensions[0]/displayDimensions[1], 0.1, 500)

    camera = Camera([-140, 2, 10], 0, 0)

    player = Player([0, 0, 0], [0, 0, 0])
    camera.rotate(player, 0, 1, 20)

    trackCoordinates = [[-200.0, -1.0, 200.0], [200.0, -1.0, 200.0], [200.0, -1.0, -200.0], [-200.0, -1.0, -200.0]]
    track = Track('track.png', trackCoordinates, camera)

    game = Game(camera, player, track)

    # track = Track('track.png')
    # coords = [[-1.0, -1.0, 1.0], [1.0, -1.0, 1.0], [1.0, -1.0, -1.0], [-1.0, -1.0, -1.0]]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
                
       # glRotatef(1, 3, 1, 1)
        glColorMask(True, True, True, True);
        glClearColor(0, 0, 0, 0);
        glClear(GL_COLOR_BUFFER_BIT);

        game.gameLoop()

        pygame.display.flip()
        
        pygame.time.wait(10)
main()
