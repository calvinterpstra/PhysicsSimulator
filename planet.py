from visual import *

class Planet:

    def __init__(self, pos, radius, color, mass, vel, accel):
        self.mass = mass
        self.vel = vel
        self.accel = accel
        self.body = sphere()
        self.body.pos = pos
        self.body.radius = radius
        self.body.color = color
        self.trail = curve(color=color)
