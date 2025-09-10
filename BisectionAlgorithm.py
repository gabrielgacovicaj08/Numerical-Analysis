import numpy as np
import math



def BisectionAlgorithm(f, a, b, TOL, maxIters):
    """
    Parameters:
        - f is the function that we are going to bisect. 
        f will be defined later on

        - a is the left sided point of the interval

        - b is the right sided point of the interval 

        - TOL is the tolerance that we want to achieve.
        if the middle point gets smaller than the TOL, that's our result

        - maxIters is the max number of iterations that we allow our algorithm to do

    Goal:
        the goal of this function is to find the root of a function through the bisection theorem 

    Returns:
        - p : float
        Approximate root.
        
        - iters : int
        Number of iterations used.
    """

    FA = f(a)
    FB = f(b)

    if (FA == 0):
        return FA, 0
    elif (FB == 0):
        return FB, 0
    elif ((np.sign(FA) * np.sign(FB)) > 0):
         raise ValueError("f(a) and f(b) must have opposite signs.")

    i = 1
    while i < maxIters:
        p = a + (b - a)/2
        FP = f(p)

        if (FP == 0 or ((b - a)/2) < TOL):
            print(p)
            return p, i
        
        i += 1
        if ((np.sign(FA) * np.sign(FP)) > 0):
            a = p
            FA = FP
        else:
            b = p

    print("couldn't evaluate the Bisection Theorem")

def f(x):
        return x**(1/2) - math.cos(x)
    
root = BisectionAlgorithm(f, a=0, b=1, TOL=1e-10, maxIters=100)
print(root)    


    