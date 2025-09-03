"""
Title: Remove K Digits to Make Smallest Number
Approach: Use monotonic increasing stack to remove larger digits while maintaining order; remove remaining k digits from end if needed
Time: O(n) where n is the length of number
Space: O(n) for stack
"""

from collections import deque

def removeKdigits(num,k):
    stack = deque()
    if k==len(num):
        return "0"
    for i in num:
        if k>0:
            while stack and stack[-1]>i:
                stack.pop()
                k-=1
                if k==0:
                    break
        stack.append(i)
    while k>0:
        stack.pop()
        k-=1
    ans = ''.join(stack).lstrip('0')
    if len(ans)==0:
        return '0'
    else:
        return ans 

num = input("Enter the Number : ")
k = int(input("Enter K : "))

ans = removeKdigits(num,k)
print("After Removing K Digit the Smallest Number is : ",ans)