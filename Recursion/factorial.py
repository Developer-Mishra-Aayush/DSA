"""
Title: Factorial using Recursion
Approach: Recursive approach where factorial(n) = n * factorial(n-1) with base case n <= 1
Time: O(n)
Space: O(n) - due to recursion stack
"""

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter the Number : "))
ans = factorial(n)
print(f"Factorial of {n} is {ans}")