#!/usr/bin/env python3

# Create the memoization dict
memo = {0:0, 1:1, 2:1}

def DPFib(n):
    """
    Dynamic programming solution for finding Fibonacci numbers using memoization
    """
    
    if n in memo.keys(): # If result already present
        return memo[n]
    
    elif n-1 in memo.keys() and n-2 in memo.keys(): # if previous results present
        memo[n] = memo[n-1] + memo[n-2]
        return memo[n]

    # If at least one of necessary previous results is present
    #elif n-1 in memo.keys(): # You cannot have n-1 present and n-2 not present; n-2 is needed for n-1
        #memo[n-2] = Fib(n-2)
    elif n-2 in memo.keys():
        memo[n-1] = DPFib(n-1)
        
    else:
        memo[n-1] = DPFib(n-1)
        memo[n-2] = DPFib(n-2)
        
    memo[n] = memo[n-1] + memo[n-2]
    return memo[n]

print([DPFib(x) for x in range(0,50)])
