from planet import *

planets = []

planet1 = Planet(pos = vector(10,0,0),
               radius = 0.7 ,
               color = color.blue,
               mass = 1,
               vel = vector(0,20,0),
               accel = vector(0,0,0))
planet2 = Planet(pos = vector(0,0,20),
               radius = 0.3 ,
               color = color.green,
               mass = 1,
               vel = vector(0,10,0),
               accel = vector(0,0,0))
planet3 = Planet(pos = vector(0,15,-20),
               radius = 0.3 ,
               color = color.red,
               mass = 1,
               vel = vector(5,-4,0),
               accel = vector(0,0,0))
planet4 = Planet(pos = vector(-10,-10,-10),
               radius = 1.2 ,
               color = color.orange,
               mass = 4,
               vel = vector(0,-15,5),
               accel = vector(0,0,0))
star = Planet(pos = vector(0,0,0),
             radius = 2,
             color = color.yellow,
             mass = 400,
             vel = vector(0,0,0),
             accel = vector(0,0,0))

planets.extend((star, planet1, planet2, planet3, planet4))

gravConstant = 10

def getGAccel(p1, p2):
    rVect = p1.body.pos - p2.body.pos
    accel = -((gravConstant * p2.mass) / rVect.mag2)
    accel *= rVect.norm()
    return accel

dt = 0.01
t = 0
while true:
    rate(100)
    for planet1 in planets:
        for planet2 in planets:
            if planet1 != planet2:
                planet1.vel += getGAccel(planet1, planet2) * dt

    for planet in planets:
        planet.body.pos += planet.vel * dt

    for planet in planets:
        planet.trail.append(pos=planet.body.pos)
    
    t += dt
