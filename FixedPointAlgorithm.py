def FixedPoint(f, p0, TOL, maxIter):
    i = 1
    while (i <= maxIter):
        p = f(p0)
        if (abs(p - p0) < TOL):
            return p, i
        else:
            i += 1
            p0 = p
    raise("Couldn t approximate the answer")

def f(x):
    return 0.5 * (10 - x**3)**0.5


root = FixedPoint(f, p0 = 0, TOL = 1e-4, maxIter= 100 )
print(root)
