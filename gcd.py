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

""" #################### Summary ####################

Not much to show here but how to implement Euclid's algorithm both ways

Once again, Iterative is faster, and here, by using the while loop, iterative is also just as neat

"""
