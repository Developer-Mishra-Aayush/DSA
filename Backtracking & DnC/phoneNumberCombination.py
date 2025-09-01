"""
Title: Letter Combinations of Phone Number
Approach: Use backtracking to generate all possible combinations by trying each letter for each digit
Time: O(4^n * n) where n is the number of digits and 4 is max letters per digit
Space: O(n) for recursion stack and result storage
"""

class Solution(object):
    def solve(self,dict,digits,ans,tempAns,i):
        if i>=len(digits):
            ans.append(tempAns)
            return
        else:
            currentC = digits[i]
            mappedC = dict[digits[i]]
            for mC in mappedC:
                # tempAns+=mC
                self.solve(dict,digits,ans,tempAns+mC,i+1)
                # tempAns = str(list(tempAns).pop())

    def letterCombinations(self, digits):
        dict = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if not digits:
            return []
        ans = []
        i = 0
        tempAns = ''
        self.solve(dict,digits,ans,tempAns,i)
        return ans