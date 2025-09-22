from sympy import symbols, diff, cos
import math
from sympy.utilities.lambdify import lambdify

def NewtonMethod(f_expr, p0, TOL, maxIter):
    x = symbols('x')
    df_expr = diff(f_expr, x)

    f = lambdify(x, f_expr, 'math')
    df = lambdify(x, df_expr, 'math')

    i = 1

    while(i < maxIter):
        

        p = p0 - (f(p0)/df(p0))
        
        if (abs(p - p0) < TOL):
            return p, i
        
        i += 1 
        p0 = p
    
    raise("Couldn't approximate the answer")

x = symbols('x')
f_expr = cos(x) - x

root = NewtonMethod(f_expr, p0 = (math.pi/4), TOL = 1e-4, maxIter = 50)
print(root)