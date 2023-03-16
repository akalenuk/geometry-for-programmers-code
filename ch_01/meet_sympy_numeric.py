from sympy import *

# Va - Amsterdam train speed
# Vp - Paris train speed
Va, Vp = symbols('Va Vp')

solution = solve([
    Vp - Va * 2,
    Va * 1 + Vp * 1 - 450
], (Va, Vp))

print(solution)
