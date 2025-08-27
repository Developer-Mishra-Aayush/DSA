"""
Title: Fibonacci Series using Recursion
Approach: Recursive approach where fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) with base cases n == 0 or n == 1
Time: O(2^n) - exponential due to repeated calculations
Space: O(n) - due to recursion stack
"""

def fibonacciSum(n):
    if n==0 or n==1:
        return n
    else:
        sum = fibonacciSum(n-1) + fibonacciSum(n-2)
        return sum

n = int(input("Enter the Nth :"))
ans = fibonacciSum(n)
print(f"Sum of Fibonacci Upto {n} is {ans}")