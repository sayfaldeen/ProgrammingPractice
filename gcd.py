#!/usr/bin/env python3

import time

"""
Script to find the Greatest Common Denominatory using Euclid's algorithm

The algorithm divides the two numbers by each other and checks for a remainder,
    if there is a remainder, then you divide the smaller value by the remainder
    and keep going until there is no more remainder

The alogrithm will be implemented 2 ways:
    1) Iteratively
    2) Recursively

"""

def Iter(n1,n2):
    "Iterative implementation"

    a,b = sorted([n1,n2], reverse=True)

    r = None
    while r != 0:
        r = a % b # remainder
        a = b
        b = r

    return a # The GCD


def Rec(n1,n2):
    a,b = sorted([n1,n2], reverse=True)

    r = a % b
    if r == 0: # base-case
        return b
    else:
        return Rec(b,r)


ts = time.time()
print(Iter(210,45))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(Rec(210,45))
print(f"Recursive solution took {round(time.time() - ts,6)} seconds")


""" #################### Results ####################
15
Iterative solution took 2.1e-05 seconds
15
Recursive solution took 1e-05 seconds
"""


""" #################### Summary ####################

Recursive implementation is actually faster here as well. This may be due to the additional assignments necessary
    within the while-loop.

Once again, the simplicity of the recursive function is beneficial.
"""
