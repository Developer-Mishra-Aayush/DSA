"""
Title: First Non-Repeating Character in a Stream
Approach: Maintain frequency map and a queue of candidates; for each char, update freq and pop from front while freq>1; append current answer
Time: O(n) amortized
Space: O(1) freq (fixed alphabet) + O(n) queue
"""

from collections import deque

def firstNonRepeating(s):
    stack = deque()
    ans = ""
    dict = {}
    for i in s:
        stack.append(i)
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1

        while stack:
            if dict[stack[0]]==1:
                ans+=stack[0]
                break
            else:
                stack.popleft()
        if len(stack)==0:
            ans+='#'
    return ans

s = input("Enter the String : ")
ans = firstNonRepeating(s)
print("Ans is : ",ans)