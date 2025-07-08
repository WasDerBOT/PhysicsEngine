from numpy import array
from pygame import draw
from numpy import float64
from math import pi, sqrt

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

    def mapping(self, r: array, reverse=False) -> array:
        if reverse:
            return (r - array([WIDTH / 2, HEIGHT / 2])) / self.scale + self.pos
        return self.scale * (r - self.pos) + array([WIDTH / 2, HEIGHT / 2])

    def do_scale(self, r):
        return r * self.scale

    def scale_itself(self, n):
        if n > 0:
            self.scale *= 1.1
        else:
            self.scale *= 0.9
        self.scale = min(3, max(0.1, self.scale))

    def shift(self, delta: array):
        self.pos += delta


# xi = 2xi - xi-1 + adt**2
class Particle:
    def __init__(self, pos, mass, charge, density=1, color=WHITE):
        self.acceleration = 0
        self.pos = pos
        self.mass = mass
        self.prev_pos = pos
        self.charge = charge
        self.color = color
        self.density = density
        self.size = sqrt((self.mass / pi)) * 30

    def apply_force(self, force):
        self.acceleration = force / self.mass

    def draw(self, drawer, screen, cam):
        drawer.circle(screen, self.color, cam.mapping(self.pos), cam.do_scale(self.size))

    def verlet_integration(self, dt):
        temp = self.pos
        self.pos = 2 * self.pos - self.prev_pos + self.acceleration * dt ** 2
        self.prev_pos = temp
        self.acceleration = 0
