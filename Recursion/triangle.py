"""
Title: Triangle Minimum Path Sum (Recursive)
Approach: At each cell (i, j), recursively choose the minimum of the two options: down (i+1, j) or down-right (i+1, j+1) and add current value.
Time: O(2^n) without memoization (n = number of rows)
Space: O(n) recursion depth
"""

def solve(triangle,i,j,sumi):
    if i>=len(triangle):
        return sumi
    else:
        # Consider First
        case1 = triangle[i][j] + solve(triangle,i+1,j,sumi)

        # Consider Second
        case2 = triangle[i][j] + solve(triangle,i+1,j+1,sumi)
        sumi = min(case1,case2)
        return sumi

def minimumTotal(triangle):
    i = 0
    j = 0
    sumi =0
    ans = solve(triangle,i,j,sumi)
    return ans

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
ans = minimumTotal(triangle)
print("Minimum Trianlge is : ",ans)