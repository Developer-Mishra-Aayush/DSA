def isPossible(nums,x):
    dict = {}
    for i,val in enumerate(nums):
        if val not in dict:
            dict[val] = i
    for i,val in enumerate(nums):
        if val-x in dict and dict[val-x]!=i:
            return True
        elif x-val in dict and dict[x-val]!=i:
            return True
    return False

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)
x = int(input("Enter the X : "))

ans = isPossible(nums,x)
print("Is Exists : ",ans)