def threeCommon(num1,num2,num3):
    len1 = len(num1)
    len2 = len(num2)
    len3 = len(num3)
    i,j,k = (0,0,0)
    ans = []
    while i<len1 and j<len2 and k<len3:
        if num1[i]==num2[j]==num3[k]:
            ans.append(num1[i])
            i+=1
            j+=1
            k+=1
        elif num1[i]<num2[j] or num1[i]<num3[k]:
            i+=1
        elif num2[j]<num1[i] or num2[j]<num3[k]:
            j+=1
        else:
            k+=1
    if ans:
        return ans
    else:
        return -1

num1 = [1,5,10,20,40,80]
num2 = [6,7,20,80,100]
num3 = [3,4,15,20,30,70,80,120]

ans = threeCommon(num1,num2,num3)
print("Common Element In Three Sorted Array is : ",ans)