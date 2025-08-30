"""
Title: Valid Anagram
Approach: Sort both strings and compare equality; alternative is frequency count dictionary.
Time: O(n log n)
Space: O(1) or O(n) depending on sort implementation
"""

def isValid(s,t):
    return sorted(s)==sorted(t)

s = input("Enter the String : ")
t = input("Enter the String : ")

ans = isValid(s,t)
print("Is Valid Anagram : ",ans)