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
    # calculating f(x) on the interval extremes 
    FA = f(a)
    FB = f(b)


    if (FA == 0):
        return FA, 0
    elif (FB == 0):
        return FB, 0
    
    # if the multiplication of the sign gives a positive result 
    # it means that the extremes of the interval are on the same side 
    # of the x axis 
    elif ((np.sign(FA) * np.sign(FB)) > 0):
         raise ValueError("f(a) and f(b) must have opposite signs.")


    i = 1
    while i < maxIters:
        # calculate the middle point 
        p = a + (b - a)/2

        # evaluate f(x) on the middle point 
        FP = f(p)

        # checking if f(p) is the actual root or if the gap between the 
        # extreme points is less than the tollerance.
        # if so we return the p point and number of iterations 
        if (FP == 0 or ((b - a)/2) < TOL):
            return p, i
        
        i += 1

        # we multiply the sign of the left extreme evaluation with the midpoint
        # evaluation and if the result is greater than 0 then we set a = p so 
        # we moving the left extreme to the mid point 
        if ((np.sign(FA) * np.sign(FP)) > 0):
            a = p
            FA = FP
        else:
            b = p

    print("couldn't evaluate the Bisection Theorem")

# defining f(x)
def f(x):
        return x**3-7*x**2+14*x-6
    
root = BisectionAlgorithm(f, a=0, b=1, TOL=1e-2, maxIters=100)
print(root)    


    