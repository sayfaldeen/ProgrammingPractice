#!/usr/bin/env python3

import time

"""
Script to perform binary search

The binary search algorithm is an algorithm to find a specific item in an ORDERED list. The trick is to
jump to the middle of the list and check if the item you want is larger or smaller then the middle item. If
the item is larger then repeat the process with the right side of the list, elsewise repeat with the left side.
NOTE: This will only work with an data structure

The algorithm will be implemented in 2 ways:
    1) Iterative
    2) Recursive

"""



def Iter(data, item):
    "Iterative implementation"

    if not data[0] <= item <= data[-1]:
        print(f"Item {item} not in data")
        return None

    elif data[0] == item:
        return 0
    elif data[-1] == item:
        return len(data) -1


    mid_index = len(data) // 2
    while data[mid_index] != item:
        
        if data[mid_index] < item:

            # Generate a new mid point for the other side of 
            mid_index += len(data[mid_index:])//2 # since we don't want to include the mid_point
        
        else:
            mid_index = len(data[:mid_index+1])//2

    return mid_index


def Rec(data, item, index=0):
    "Recursive implementation"

    if not data[0] <= item <= data[-1]:
        print(f"Item {item} not in data")
        return None

    elif data[0] == item:
        return 0
    elif data[-1] == item:
        return len(data) -1

    mid = len(data) // 2

    if data[mid] == item:
        return mid + index # since I am subsetting the data each time (saves memory) we need to track
                            # what index we are still on relative to the original data
    else:
        # Check the adjacent items to reduce recursion
        if data[mid-1] == item:
            return mid -1 + index
        elif data[mid+1] == item:
            return mid +1 + index

        elif data[mid] > item:
            return Rec(data[:mid+1], item) # Need +1 to mid at the end, because the slice does not include
                                            # the point of the slice
        else:
            return Rec(data[mid+1:], item, index+mid+1)


data = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
item = -1

ts = time.time()
print(Iter(data, item))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")

ts = time.time()
print(Rec(data, item))
print(f"Iterative solution took {round(time.time() - ts,6)} seconds")



""" #################### Summary ####################
This was a perfect example of recursion making it easier to solve this problem (at least for me).

The recursive solution is also faster but that is because of my 'adjacent search' heuristic, which became annoying 
    to implement with the iterative approach due to my use of the while loop.

Recursion just makes finding an efficient solution easier in ones head and makes the implementation a little more 
    straightforward and enables the use of some heuristics more easily and efficiently

"""
