from collections import deque
#User Template for python3


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.isNullFound = False
        
    #Your Function Should return True/False
    def isHeap(self, root):
        queue = deque()
        queue.append(root)
        
        while queue:
            temp = queue.popleft()
            if temp is None:
                self.isNullFound = True
            
            else:
                if self.isNullFound:
                    return False
                checkCondition = (temp.right and temp.data>temp.right.data) or \
                (temp.left and temp.data >temp.left.data)
                if checkCondition == False:
                    return False
                queue.append(temp.left)
                queue.append(temp.right)
        return True