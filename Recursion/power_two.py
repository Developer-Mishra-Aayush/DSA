"""
Title: Power of Two using Recursion
Approach: Recursive approach where powerOfTwo(n) = 2 * powerOfTwo(n-1) with base case n < 1
Time: O(n)
Space: O(n) - due to recursion stack
"""

def powerOfTwo(n):
    if n<1:
        return 1
    else:
        sum = 2*powerOfTwo(n-1)
        return 

n = int(input("Enter the Power of 2 : "))
ans = powerOfTwo(n)
print(f"Two Power of {n} is {ans}")