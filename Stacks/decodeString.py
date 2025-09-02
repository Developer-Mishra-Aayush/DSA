"""
Title: Decode String (k[encoded_string])
Approach: Use stack to build substrings and repeat counts; on ']' pop until '[' and expand
Time: O(n) where n is length of string
Space: O(n) for stack
"""
from collections import deque
def decodeString(s):
    stack = deque()
    for i in s:
        if i!=']':
            stack.append(i)
        else:
            curr = ''
            while stack[-1]!='[':
                curr=stack.pop()+curr
            stack.pop()
            curr_num = ''
            while stack and stack[-1].isdigit():
                curr_num = stack.pop() + curr_num
            new_data = int(curr_num)*curr
            stack.append(new_data)
    return ''.join(stack)

s = input("Enter the String : ")
ans = decodeString(s)
print("Decode String is : ",ans)