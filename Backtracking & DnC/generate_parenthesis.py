"""
Title: Generate Parentheses
Approach: Use backtracking to generate valid parentheses by adding '(' or ')' when valid
Time: O(4^n/sqrt(n)) - Catalan number complexity
Space: O(n) for recursion stack and result storage
"""

def solve(n,open,close,ans,temp):
    if open == 0 and close ==0:
        ans.append(temp)
        return
    else:
        # Include Open Bracket
        if open>0:
            solve(n,open-1,close,ans,temp+'(')
        # Include Close Bracket
        if close>open:
            solve(n,open,close-1,ans,temp+')')

def generateParenthesis(n):
    if n==1:
        return '()'
    else:
        open = n
        close = n
        ans = []
        temp = ''
        solve(n,open,close,ans,temp)
        return ans

n = int(input("Enter the N : "))
ans = generateParenthesis(n)
print("Total Possible Parenthesis is : ",ans)