from functools import lru_cache

@lru_cache(None)
def solve(n):
    if n==0:
        return 0
    if n<0:
        return float('inf')
    else:
        mini = float('inf')
        for i in range(1,int(n**0.5) + 1):
            if i*i<=n:
                mini = min(mini,1+solve(n-i*i))
        return mini


def numSquare(n):
    if n==0:
        return 0
    ans = solve(n)
    return 

n = int(input("Enter the Number : "))
ans = numSquare(n)
print("Least Number of Perfect Square numbers that sum n : ",ans)