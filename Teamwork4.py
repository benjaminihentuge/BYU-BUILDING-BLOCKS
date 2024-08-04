import math
m = float(input('mass (in kg)'))
g = float(input('acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)'))
t = float(input('time (in seconds)'))
P = float(input('density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)'))
A = float(input('cross sectional area of projectile (in square meters)'))
C = float(input('drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)'))

print()
c = (1/2) * P * A * C
print (f'the value of c {c:.3f}')
v = math.sqrt (m * g / c) * (1 - math.exp (- math.sqrt(m * g * c) / m * t)) 
print (f'the overall velocity after {t} is {v:.3f} m/s')