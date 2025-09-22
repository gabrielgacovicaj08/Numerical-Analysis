import math

def SecantMethod(f, p0, p1, TOL, maxIter):
    q0 = f(p0)
    q1 = f(p1)

    i = 2
    while (i < maxIter):
        p = p1 - (q1 * (p1 - p0)/(q1 - q0))

        if (abs(p - p1) < TOL): 
            return p, i

        i += 1 

        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)

    raise("Couldn't approximate the answer") 

def f(x):
    return math.cos(x) - x

root = SecantMethod(f, p0 = 0.5, p1 = (math.pi)/4, TOL = 1e-4, maxIter=10)
print(root)