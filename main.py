import pygame
import sys
from numpy import array
from Physics_classes import Camera
from Physics_classes import Particle
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
running = True


class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.size = 40



Cam = Camera(array([0, 0]), 1)
Objects = []
Objects.append(Particle( array([0, 0]), 1, 1, RED))

isShifting = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            Cam.scale_itself(event.y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                p0 = array(pygame.mouse.get_pos())
                isShifting = True
                p1 = p0

        elif isShifting and event.type == pygame.MOUSEMOTION:
            Cam.shift((p1 - p0) * 1 / Cam.scale)
            p1 = array(pygame.mouse.get_pos())
            Cam.shift((p0 - p1) * 1 / Cam.scale)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                isShifting = False

    keys = pygame.key.get_pressed()

    screen.fill(BLACK)
    for obj in Objects:
        obj.draw(drawer=pygame.draw, screen=screen, cam=Cam)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
