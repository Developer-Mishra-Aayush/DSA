"""
Title: Remove All Occurrences of Substring (Recursive)
Approach: While the pattern exists, remove it and recurse until no occurrence remains
Time: O(k * n) worst-case depending on replacements (k occurrences)
Space: O(k) recursion depth due to repeated removals
"""

def removeOccurence(s,part):
    if s.find(part)!=-1:
        s = s.replace(part,'')
        return removeOccurence(s,part)
    return s

s = "daabcbaabcbc"
part = "abc"
ans = removeOccurence(s,part)
print("After Removing All Occurence of Part From a String : ",ans)