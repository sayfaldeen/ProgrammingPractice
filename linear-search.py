#!/usr/bin/env python3

import time

"""
This script will explore the linear search algorithm.
This algorithm is based on iterating through an UNORDERED data structure WITHOUT REPEATS and returning the
    index of a specific item of interest.

The algorithm will be implemented in 3 different ways:
    1) Iteratively
    2) List comp
    3) Recursively

"""



def Iter(data, item):
    "Iterative implementation"

    for n,i in enumerate(data):
        if i == item:
            return n
    
    # If nothing is returned
    print(f"Item {item} is not in data")
    return None


def Iter2(data, item):
    "Iterative implementation"

    n = -1 # To make us start at 0 in the loop
    for i in data:
        n += 1
        if i == item:
            return n        

    
    # If nothing is returned
    print(f"Item {item} is not in data")
    return None


def Iter3(data, item):
    "Iterative implementation"

    for n,i in enumerate(data,0):
        if i == item:
            return n
    
    # If nothing is returned
    print(f"Item {item} is not in data")
    return None


def Iter4(data, item):
    "Iterative implementation"

    for n,i in enumerate(data, start=0):
        if i == item:
            return n
    
    # If nothing is returned
    print(f"Item {item} is not in data")
    return None


def ListComp(data,item):
    res = [n for n,i in enumerate(data, 0) if i == item]

    if len(res) > 0: # Make sure we got a result
        return res[0]
    else: # If not, then item is not in data
        print(f"Item {item} is not in data")
        return None


def Rec(data, item, n=0):
    "Recursive implementation"

    if n == len(data): # Ensure that item is in list
        print(f"Item {item} is not in data")
        return None

    else:
        if data[n] == item: # base-case
            return n
        else: # recurse
            return Rec(data, item, n+1)



data = [0,2,4,6,1,9,8, 11, 14,13, 7, 15,19,16,18,21,29,20,25]
item = 8


ts = time.time()
print(Iter(data, item))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(Iter2(data, item))
print(f"Iterative solution WITHOUT ENUMERATE took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(Iter3(data, item))
print(f"Iterative solution WITH ENUMERATE BUT WITH START=0 took {round(time.time() - ts,6)} seconds")


ts = time.time()
print(ListComp(data, item))
print(f"List comp solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(Rec(data, item))
print(f"Recursive solution took {round(time.time() - ts,6)} seconds")



""" #################### Summary ####################

This time, we get a surprise; The RECURSIVE solution was the FASTEST [before adding the iterative functions]
Why? Well, it's because we don't need the enumerate function or to enumerate our position and 
    instead we can just add 1 to the position variable (n in our recursive function)

So what happens when we remove the enumerate function in the iterative solution? It gets way faster and
    becomes even faster than the recursive solution.

Final question; why does enumerate() have such a big hit on performance? Partially because of the fact that 
    enumerate() needs to know the length. If no start value is given, the function has to check that there is a 
    zero index. Also if a keyword is given, then the function has to perform keyword matching which will also
    slow the code down. If we give enumerate() a start but without a keyword, it is just as fast as using
    the n += 1 solution. This is an interesting look at the difference in performance that can arise depending
    on how these built-in functions are created and a great thing to consider going forward. That being said, 
    the performace hit from using the keyword will be very small with bigger data and more complex operations,
    so this reall needs to be weighed against readability. Mainly, don't use keywords if the function needs to be
    called many times and thus will need to perform the keyword matching many times

"""
