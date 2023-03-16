from sympy import *

# Va - Amsterdam train speed
# Vp - Paris train speed
# Vpx - a ratio Vp/Va (used to be 2)
# D - the distance in between Paris and Amsterdam (450)
# t - the time before the trains meet (1)
Va, Vp, Vpx, D, t = symbols('Va Vp Vpx D t')

solution = solve([
    Vp - Va * Vpx,
    Va * t + Vp * t - D
], (Va, Vp))

print(solution)
print(pycode(solution))
print(latex(solution))
