def spiral_print(nums):
    sRow = 0
    sCol = 0
    eRow = len(nums)-1
    eCol = len(nums[0])-1
    totalElement = len(nums)*len(nums[0])
    ans = []
    while len(ans)<totalElement:
        # Printing Starting Row
        if sRow<=eRow:
            for i in range(sCol,eCol+1):
                ans.append(nums[sRow][i])
            sRow+=1
        # Printing Ending Column
        if sCol<=eCol:
            for i in range(sRow,eRow+1):
                ans.append(nums[i][eCol])
            eCol-=1
        # Printing Ending Row
        if sRow<=eRow:
            for i in range(eCol,sCol-1,-1):
                ans.append(nums[eRow][i])
            eRow-=1
        # Printing Starting Column
        if sCol<=eCol:
            for i in range(eRow,sRow-1,-1):
                ans.append(nums[i][sCol])
            sCol+=1
    return ans

nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]
ans = spiral_print(nums)
print("Apiral Print OF A Matrix is : ",ans)