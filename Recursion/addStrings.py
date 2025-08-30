"""
Title: Add Two Strings (Recursive)
Approach: Process digits from right to left with carry; recurse on indices and append digit results, reverse at the end
Time: O(max(n, m)) where n, m are lengths of inputs
Space: O(max(n, m)) due to recursion stack and result building
"""

def solve(num1,num2,index1,index2,ans,carry):
    if index1<0 and index2<0:
        if carry:
            ans.append(str(carry))
            print("carry is : ",carry)
            print(ans)
        return ''.join(ans)[::-1]
    else:
        n1 = num1[index1] if index1>=0 else 0
        n2 = num2[index2] if index2>=0 else 0
        tempAns = int(n1) + int(n2) + carry
        carry = 0
        print("Num1 is : ",n1," Num2 is : ",n2," Carry is ",carry,"And sum is : ",tempAns)
        if tempAns>9:
            carry = 1
            tempAns = tempAns%10
        ans.append(str(tempAns))
        print("Ans is : ",ans)
        result = solve(num1,num2,index1-1,index2-1,ans,carry)
        return result



def addRE(num1,num2):
    if not num1 and num2:
        return '0'
    if not num1:
        return num2
    if not num2:
        return num1
    else:
        index1 = len(num1)-1
        index2 = len(num2)-1
        ans = []
        carry = 0
        ans = solve(num1,num2,index1,index2,ans,carry)
        return ans



# num1 = "11"
# num2 = "123"
num1 = "456"
num2 = "77"
ans = addRE(num1,num2)
print("Addition is : ",ans)