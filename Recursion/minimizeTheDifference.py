"""
Title: Minimize the Difference (Matrix Rows to Target)
Approach: Intended recursive/DP approach: pick one value from each row to minimize |sum - target|; typical solutions use recursion with memoization or DP over sums
Time: Exponential without memoization; DP ~ O(rows * targetRange)
Space: O(rows) recursion depth or DP table size
"""

# def solve(mat,target,i,j):
#     for row in range(len(mat)):




# def minimizeTheDifference(mat,target):
#     ans = solve(mat,target,0,0)
#     return ans



# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# target = 13
# ans = minimizeTheDiffernece(mat,target)
# print("minimum DIfference is : ",ans)