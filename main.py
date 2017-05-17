from planet import *

radiusScaleFactorSun = 50
radiusScaleFactorPlanets = 500
earth = Planet(pos = vector(149.6 * math.pow(10,9),0,0),
               radius = 6.371 * math.pow(10,6) * radiusScaleFactorPlanets,
               color = color.green,
               mass = 5.972 * math.pow(10, 24),
               initialVel = vector(0,30000,0),
               initialAccel = vector(0,0,0))
sun = Planet(pos = vector(0,0,0),
             radius = 695.7 * math.pow(10,6) * radiusScaleFactorSun,
             color = color.yellow,
             mass = 1.989 * math.pow(10,30),
             initialVel = vector(0,0,0),
             initialAccel = vector(0,0,0))

t = 0
while true:
    rate(10)

    fnetEarth = (double(6.67*math.pow(10,-11))*double(earth.mass)*double(sun.mass))/(math.pow((earth.body.pos - sun.body.pos).mag,2))
    fnetEarthVect = fnetEarth*norm(earth.body.pos - sun.body.pos)
    accelEarthVect = fnetEarthVect/earth.mass
    print(mag(earth.initialVel + accelEarthVect*t))
    earth.body.pos += earth.initialVel*t + (1/2)*accelEarthVect*math.pow(t,2)
    
    
    t = t+1
