"""
Title: Print All Subsequences of a String (Recursive)
Approach: Recursive inclusion-exclusion: at each index, either include the character or exclude it, accumulate results in list
Time: O(2^n * n) - 2^n subsequences, up to n to copy/concatenate
Space: O(n) recursion depth; output list holds O(2^n) strings
"""

def printSubsequence(s,index,temp_ans,ans):
    if index>=len(s):
        ans.append(temp_ans)
        return
    else:
        # Exclude Case
        printSubsequence(s,index+1,temp_ans,ans)

        # Include Case
        
        printSubsequence(s,index+1,temp_ans+s[index],ans)

s = input("Enter the String : ")
ans = []
temp_ans = ""

printSubsequence(s,0,temp_ans,ans)
print("All Subsequence of a string is : ",ans)