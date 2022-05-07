#!/usr/bin/env python3

"""
Code to implement the quickselect algorithm. The algorithm operates by semi-sorting the data to find a specific
    index within the sorted structure e.g. k=1 would be the minimum value, k=2 would be second lowest, etc...

Algorithm Overview:
    1) Choose a random pivot within the data
    2) Find the pivot_index (index of the pivot item)
        - This is done by moving all of the value that are lower than pivot to the left (semi-sorting)
    3) If pivot index is > k, only look at the left side of the partition, else take the right side
    4) Keep going until pivot_index == k

The algorithm will be implemented in two ways:
    1) Iteratively
    2) Recursively

"""

import time
import random

def Iter(data, k):
    "Iterative implementation"
    
    if not 0 < k <= len(data) and len(data) > 0:
        print(f"k={k} is not appropriate size for data of size {len(data)}")
        return None
    
    if len(data) == 1:
        return data[0]


    # Start the while loop
    pivot_index = None
    while pivot_index != k-1:

        start = 0
        end = len(data) -1

        # Find the random pivot
        pivot = data[random.randint(start,end)]

        # Partition the data and find the pivot index
        lower = []
        higher = []

        [lower.append(x) if x < pivot 
                else higher.append(x) if x > pivot
                else None
                for x in data]

        pivot_index = len(lower)


        if pivot_index > k: # Take the left (lower) side
            start = start
            end = pivot_index-1

        else:
            start = pivot_index + 1
            end = end

        # Add the partitions back into one dataset
        lower.append(pivot)
        lower.extend(higher)
        data = lower

    return pivot
            



def Rec(data,k):
    "Recursive implementation"

    # Make sure the parameters are appropriate
    if not 0 < k <= len(data):
        print(f"k={k} is not appropriate for data of length {len(data)}")
        return None

    if len(data) == 1:
        return data[0]

    # Partition the data
    pivot = data[random.randint(0, len(data)-1)] # -1 because window includes the end
    lower = []
    higher = []
    [lower.append(x) if x < pivot
            else higher.append(x) if x > pivot
            else None
            for x in data]
    
    pivot_index = len(lower)
    
    if pivot_index == k-1:
        return pivot

    if pivot_index > k:
        return Rec(lower, # lower partition 
                k)
    else:
        return Rec(higher, # use the higher partition going forward
                k - pivot_index-1) # subtract the pivot index, because we have removed that many spots from the data 
                                    # and we take one more because we are also removing the pivot

    


data = [3,0,4,200,5,10,2,7]
k = 8

ts = time.time()
print(Iter(data,k))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(Rec(data,k))
print(f"Recursive solution took {round(time.time() - ts,6)} seconds")


""" #################### Results ####################
200
Iterative solution took 5.2e-05 seconds
200
Recursive solution took 2.1e-05 seconds
"""


""" #################### Summary ####################

Interestingly, the RECURSIVE solution was FASTER. This is possible due to us recombining the lower, pivot, and higher data into one strucutre. This was the 
    most intuitive solutuion to me within the while loop and changing it around after I had already written the code was getting messy. The increased efficiency
    we get with the recursive code is also much neater to implement as you can that the recursive code is shorter and much easier to follow.

"""
