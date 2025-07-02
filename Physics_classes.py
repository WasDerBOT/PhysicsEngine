from numpy import array
from pygame import draw
from numpy import float64
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class Camera:
    def __init__(self, pos: array, scale):
        self.pos = pos
        self.pos = self.pos.astype(float64)
        self.scale = scale

    def move(self, dif: array):
        self.pos += dif

    def mapping(self, r: array) -> array:
        return self.scale * (r - self.pos) + array([WIDTH / 2, HEIGHT / 2])

    def do_scale(self, r):
        return r * self.scale

    def scale_itself(self, n):
        if n > 0:
            self.scale *= 1.1
        else:
            self.scale *= 0.9

    def shift(self, delta: array):
        self.pos += delta


class Particle:
    def __init__(self, pos, mass, charge, color = WHITE, velocity = array([0, 0])):
        self.pos = pos
        self.mass = mass
        self.charge = charge
        self.color = color

    def apply_force(self, force, dt):
        self.velocity += dt * force / self.mass

    def draw(self, drawer, screen, cam):
        drawer.circle(screen, self.color, cam.mapping(self.pos), cam.do_scale(self.mass * 30))


