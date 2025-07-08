import pygame
import sys
from numpy import array
from Physics_classes import Camera
from Physics_classes import Particle

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")

FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
running = True

T = 1 / FPS


class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.size = 40


def norm(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5


Cam = Camera(array([0, 0]), 1)
Objects = []
Objects.append(Particle(array([0, 0]), 10, 1, RED))
todraw = True
isGrabbing = False
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
            if event.button == 1:
                p0 = Cam.mapping(array(pygame.mouse.get_pos()), reverse=True)
                for obj in Objects:
                    if norm(obj.pos - p0) < obj.size:
                        grab = obj
                        dx = p0 - grab.pos
                        isGrabbing = True
                        break

        elif isShifting and event.type == pygame.MOUSEMOTION:
            Cam.shift((p1 - p0) * 1 / Cam.scale)
            p1 = array(pygame.mouse.get_pos())
            Cam.shift((p0 - p1) * 1 / Cam.scale)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                isShifting = False
            if event.button == 1:
                isGrabbing = False

    keys = pygame.key.get_pressed()

    screen.fill(BLACK)
    if isGrabbing:
        grab.apply_force(dx * 100 * norm(dx))
        grab.verlet_integration(T)
        grab.prev_pos = (grab.prev_pos + grab.pos) / 2
        dx = Cam.mapping(array(pygame.mouse.get_pos()), reverse=True) - grab.pos

    for obj in Objects:
        obj.verlet_integration(T)
        obj.draw(drawer=pygame.draw, screen=screen, cam=Cam)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
