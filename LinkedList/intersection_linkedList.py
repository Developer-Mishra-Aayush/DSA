class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLength(self,A):
        i = 0
        temp = A.head
        while temp:
            temp = temp.next
            i+=1
        return i
    
    def getIntersectionNode(self,A,B):
        if A.head is None:
            return None
        if B.head is None:
            return None
        else:
            len1 = self.getLength(A)
            len2 = self.getLength(B)
            temp1 = A.head
            temp2 = B.head
            if len1>len2:
                requiredLength = len1-len2
                i = 0
                temp1 = A.head
                while i<requiredLength:
                    temp1 = temp1.next
                    i+=1
            if len2>len1:
                requiredLength = len2-len1
                i = 0
                temp2 = B.head
                while i<requiredLength:
                    temp2 = temp2.next
                    i+=1
            while temp1!=temp2 and temp1 is not None and temp2 is not None:
                temp1 = temp1.next
                temp2 = temp2.next
                if temp1 == temp2:
                    return temp1
            return None
        
A = LinkedList()
A.head = Node('a1')
second = Node('a2')
third = Node('c1')
fourth = Node('c2')
fifth = Node('c3')

A.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

B = LinkedList()
B.head = Node('b1')
second1 = Node('b2')
third1 = Node('b3')
B.head.next = second1
second1.next = third1
third1.next = third
ans = A.getIntersectionNode(A,B)
print("Intersection Node is : ",ans.data)