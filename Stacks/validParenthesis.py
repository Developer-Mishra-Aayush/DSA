from collections import deque

def isValid(s):
    stack = deque()
    i=  0
    opened = ['[','(','{']
    closed = [']',')','}']
    while i<len(s):
        stackBracket=''
        if not stack and s[i] in closed:
            return False
        elif not stack or s[i] in opened:
            stack.append(s[i])
            i+=1
        elif s[i] in closed:
            if s[i] == ']':
                stackBracket = '['
            elif s[i] == '}':
                stackBracket = '{'
            elif s[i] == ')':
                stackBracket = '('
            if stackBracket!=stack[-1]:
                return False
            else:
                ans = stack.pop()
                i+=1
        else:
            return False
    if not stack:
        return True
    else:
        return False

s = input("Enter the String : ")
ans = isValid(s)
print("Is Valid Parenthesis : ",ans)