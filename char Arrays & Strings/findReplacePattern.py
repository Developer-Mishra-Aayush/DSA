"""
Title: Find and Replace Pattern
Approach: For each word, check bijective mapping to pattern using two-way constraints (char->char and reverse).
Time: O(k * L) where k=#words, L=word length
Space: O(1) per word (limited alphabet)
"""

def isPossible(words,pattern):
    dict = {}
    if len(words)!=len(pattern):
        return False
    for i in range(len(words)):
        if words[i] in dict:
            if dict[words[i]]!=pattern[i]:
                return False
            else:
                continue
        elif words[i] not in dict and pattern[i] not in dict.values():
            dict[words[i]] = pattern[i]
        else:
            return False
    return True

def findReplacePattern(words,pattern):
    ans = []
    for i in words:
        if isPossible(i,pattern):
            ans.append(i)
    return ans

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

ans = findReplacePattern(words,pattern)
print("Ans is :",ans)