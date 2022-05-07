#!/usr/bin/env python3


"""
This script contains code to implement the quicksort algorithm. This algorithm is very similar to
    the previous quickselect algorithm. It partitions the data around a pivot and then recurses
    through both partitions until the data is sorted.

Algorithm overview:
    1. Partition the data
    2. Go through both partitions and repeat the same steps until the given partitions are empty

This script will only be implemented using a recursive approach. An iterative approach was getting a little messy
    and annoying to get it be neat and efficient. 

"""

import time
from random import randint


def Rec(data):
    "Recursive implementation"

    global sdata
    sdata = dict([(n,None) for n,x in enumerate(data,0)])

    _Rec(data)

    return sdata


def _Rec(data, index=0):


    global sdata

    if len(data) == 0:
        print("Data is empty")
        return None
    
    if len(data) == 1: # base-case
        sdata[index] = data[0]

    # Partition the data
    pivot = data[randint(0, len(data)-1)]

    lower = []
    higher = []
    [lower.append(x) if pivot > x 
            else higher.append(x) if x > pivot
            else None
            for x in data]

    pivot_index = len(lower)

    # Add the sorted data
    sdata[pivot_index + index] = pivot

    # Recurse through lower
    if len(lower) > 0:
        _Rec(lower, index)

    # Recurse through higher
    if len(higher) > 0:
        _Rec(higher, index+pivot_index+1)


def Rec2(data):
    "Recursive implementation"

    global sdata
    sdata = dict([(n,None) for n,x in enumerate(data,0)])

    _Rec2(data)

    return sdata


def _Rec2(data, index=0):


    global sdata

    if len(data) == 0:
        print("Data is empty")
        return None
    
    if len(data) == 1: # base-case
        sdata[index] = data[0]

    # Partition the data
    pivot = data[randint(0, len(data)-1)]

    lower = []
    higher = []
    [lower.append(x) if pivot > x 
            else higher.append(x) if x > pivot
            else None
            for x in data]

    pivot_index = len(lower)

    # Add the sorted data
    sdata[pivot_index + index] = pivot

    # Recurse through lower
    if len(lower) > 0:
        
        # Implement adjacent search heuristic to limit recursion
        if len(lower) == 1:
            sdata[pivot_index + index -1] = lower[0]
        else:
            _Rec(lower, index)

    # Recurse through higher
    if len(higher) > 0:

        # Implement adjacent search heuristic to limit recursion
        if len(higher) == 1:
            sdata[pivot_index + index +1] = higher[0]
        else:
            _Rec(higher, index+pivot_index+1)


    
data = [-2, -5, 100, 5, -200, 10, 1,2,0, 9]

ts = time.time()
print(Rec(data))
print(f"The recursive solution took {time.time() - ts :0.4e} seconds to run")

ts = time.time()
print(Rec2(data))
print(f"The recursive solution WITH 'adjacent search' took {time.time() - ts :0.4e} seconds to run")


""" #################### Results ####################
{0: -200, 1: -5, 2: -2, 3: 0, 4: 1, 5: 2, 6: 5, 7: 9, 8: 10, 9: 100}
The recursive solution took 1.2350e-04 seconds to run
{0: -200, 1: -5, 2: -2, 3: 0, 4: 1, 5: 2, 6: 5, 7: 9, 8: 10, 9: 100}
The recursive solution WITH 'adjacent search' took 7.0333e-05 seconds to run
"""

""" #################### Summary ####################

This time I only implemented the recursive approach because of the nuisance of implementing an iterative 
    approach while trying to keep it neat. This sort of algorithm also really lends itself to being implemented
    with a recursive approach.

I also experimented with an 'adjacent search heuristic' again and it speeds up the algorithm by ~2x. Anything 
    that we can do to limit the recursive calls will benefit the performance and increase the efficiency.

"""
