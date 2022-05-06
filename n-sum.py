#!/usr/bin/env python3

import time

"""
Script coding up the n-sum problem in multiple ways:
    1) Iterative
    2) List comprehension
    3) Recursively

The n-sum problem: Calculate the sum of the first N integers
"""

def IterativeSum(n):
    "Iterative implementation"

    sum = 0

    for i in range(1,n+1):
        sum += i
    
    return sum


def ListSum(n):
    "Implementation using list comprehension"

    return sum([i for i in range(1, n+1)])


def RecSum(n, Sum=0):
    "Recursive implementation"

    if n == 0: # base-case
        return Sum

    else: # recurse
        return RecSum(n-1, Sum+n)


ts = time.time()
print(IterativeSum(100))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(ListSum(100))
print(f"List comp solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(RecSum(100))
print(f"Recrusive solution took {round(time.time() - ts,6)} seconds")

""" #################### Results ####################
5050
Iterative solution took 1.2e-05 seconds
5050
List comp solution took 5e-06 seconds
5050
Recrusive solution took 2.4e-05 seconds
"""


"""
This is a good example of performance of the different appraoches

List comp is usually the fastest, followed closely by the iterative solution
    so why use recursive functions if we know they are slower than iterative solutions?
    Two main reasons:
        1) Readability of code; much neater than having a lot of branches in your code
        2) Simplcity when formulating a solution, especially for problems made up of 
            multiple sub-problems; i.e. recursion makes it easier to think in dynamic programming

With recursion though, we may crash the CPU due to too many stack calls of the function

"""
