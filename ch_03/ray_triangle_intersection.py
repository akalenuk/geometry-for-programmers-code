from sympy import *

# the point from which the ray starts
Px, Py, Pz = symbols('Px Py Pz')

# the ray’s direction vector
dx, dy, dz = symbols('dx dy dz')

# point A of the ABC triangle
Ax, Ay, Az = symbols('Ax Ay Az')

# vector A to B of the ABC triangle
ABx, ABy, ABz = symbols('ABx ABy ABz')

# vector A to C of the ABC triangle
ACx, ACy, ACz = symbols('ACx ACy ACz')

# parameters that specify the point on a ray and point on a triangle’s plane
t, u, v = symbols('t u v')

solution = solve([
    Px +t*dx - (Ax + ABx*u + ACx*v),
    Py +t*dy - (Ay + ABy*u + ACy*v), 
    Pz +t*dz - (Az + ABz*u + ACz*v)
], (t, u, v))

print('  the whole solution:')
print (pycode(solution))

print('')
print('  divisor with collected dx, dy, dz:')
print(collect(ABx*ACy*dz - ABx*ACz*dy - ABy*ACx*dz + ABy*ACz*dx + ABz*ACx*dy - ABz*ACy*dx, (dx, dy, dz)))

print('')
print('  t with collected ACx, ACy, ACz:')
print(collect(Ax*ABy*ACz - Ax*ABz*ACy - Ay*ABx*ACz + Ay*ABz*ACx + Az*ABx*ACy - Az*ABy*ACx - ABx*ACy*Pz + ABx*ACz*Py + ABy*ACx*Pz - ABy*ACz*Px - ABz*ACx*Py + ABz*ACy*Px, (ACx, ACy, ACz)))

print('')
print('  u with collected dx, dy, dz:')
print(collect(-Ax*ACy*dz + Ax*ACz*dy + Ay*ACx*dz - Ay*ACz*dx - Az*ACx*dy + Az*ACy*dx - ACx*Py*dz + ACx*Pz*dy + ACy*Px*dz - ACy*Pz*dx - ACz*Px*dy + ACz*Py*dx, (dx, dy, dz)))

print('')
print('  v with collected dx, dy, dz:')
print(collect(Ax*ABy*dz - Ax*ABz*dy - Ay*ABx*dz + Ay*ABz*dx + Az*ABx*dy - Az*ABy*dx + ABx*Py*dz - ABx*Pz*dy - ABy*Px*dz + ABy*Pz*dx + ABz*Px*dy - ABz*Py*dx, (dx, dy, dz)))
