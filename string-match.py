#!/usr/bin/env python3

import time
import numpy as np

"""
Script trying different implementations for finding the number matches between two strings of the same length

We will be working on 4 different implementations:
    1) Iterative
    2) List comprehension
    3) Numpy vectorization
    4) Recursive

"""

# Set up the strings
s1 = "ACCTTGGAAAACCCTTGGACCTTGGAAAACCCTTGGACCTTGGAAAACCCTTGG"
s2 = "AACTTGGGAACCCCTGCCAACTTGGGAACCCCTGCCAACTTGGGAACCCCTGCC"

def IterMatch(s1,s2):
    "Iterative implementation"

    matches = 0

    for n1,n2 in zip(s1,s2):
        if n1 == n2:
            matches += 1
        else:
            pass
    
    return matches


def ListMatch(s1,s2):
    "List comp implementation"
    
    return sum([1 for n1,n2 in zip(s1,s2)
            if n1 == n2])


def NumpyMatch(s1,s2):
    "Numpy vectorization approach; need to turn string into an array"

    v1,v2 = np.array([x for x in s1]), np.array([x for x in s2])

    return len(v1[v1 == v2])

def NumpyVecMatch(v1,v2):
    "Numpy implementation without needing to turn a string into an array"

    return len(v1[v1 == v2])


def RecMatch(s1,s2,matches=0):
    "Recursive implementation"

    if len(s1) == 1: # base-case; no where else to go
        if s1 == s2:
            return matches + 1
        else:
            return matches

    else: # recurse
        if s1[0] == s2[0]:
            return RecMatch(s1[1:], s2[1:], matches+1)
        else:
            return RecMatch(s1[1:], s2[1:], matches)





ts = time.time()
print(IterMatch(s1,s2))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")


ts = time.time()
print(ListMatch(s1,s2))
print(f"List comp solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(NumpyMatch(s1,s2))
print(f"Numpy solution took {round(time.time() - ts,6)} seconds")

v1,v2 = np.array([x for x in s1]), np.array([x for x in s2])
ts = time.time()
print(NumpyVecMatch(v1,v2))
print(f"Numpy solution took {round(time.time() - ts,6)} seconds WITH pre-done vectors")

ts = time.time()
print(RecMatch(s1,s2))
print(f"Recursive solution took {round(time.time() - ts,6)} seconds")


""" #################### Results ####################
36
Iterative solution took 1.2e-05 seconds
36
List comp solution took 8e-06 seconds
36
Numpy solution took 5.4e-05 seconds
36
Numpy solution took 5e-06 seconds WITH pre-done vectors
36
Recursive solution took 3.6e-05 seconds
"""


""" #################### Summary ####################

This time, numpy vectorization is the fastest, followed closely by list comp. We see a big performance hit using 
numpy vectorization if the input is not already a vector. This is because we need to turn it into a list and then a vector. Long story short, recursive was not the neatest here and there was not a good oppurtunity for dynamic 
programming which means a recursive implementation is not useful here. List comp though is a consistently good
choice AS LONG AS THE CODE STAYS READABLE.

"""
