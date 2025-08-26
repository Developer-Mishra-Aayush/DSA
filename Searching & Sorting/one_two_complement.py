"""
Title: 1's and 2's Complement
Approach: Convert to fixed-width binary, flip bits for 1's complement, then add one for 2's complement.
Time: O(bit)
Space: O(bit)
"""

def decimal_binary(num,bit):
    binary = ""
    for i in range(bit):
        binary = str(num%2) + binary
        num = num //2
    return binary

def ones_complement(nums,bit):
    binary = decimal_binary(nums,bit)
    comp = ""
    for b in binary:
        if b=='0':
            comp+='1'
        else:
            comp+='0'
    return comp

def two_complement(num,bit):
    ones = ones_complement(num,bit)
    ones = list(ones)
    carry = 1
    for b in range(bit-1,-1,-1):
        if ones[b]=="1" and carry ==1 :
            ones[b] = "0"
        elif ones[b] == "0" and carry ==1:
            ones[b]="1"
            carry = 0
        else:
            continue
    return ''.join(ones)
        
num = int(input("Enter the Number :"))
bit = int(input("Enter the Bit :"))
ans = ones_complement(num,bit)
print("Ones Complement is : ",ans)
ans = two_complement(num,bit)
print("Two Complement is : ",ans)