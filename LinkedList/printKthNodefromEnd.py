"""
Title: Kth Node from End in Linked List
Approach: Compute length, move (len-k-1) steps to get the previous node, then return next; two-pointer alt.
Time: O(n)
Space: O(1)
"""

class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLength(self):
        i = 0
        temp = self.head
        while temp:
            temp = temp.next
            i+=1
        return i

    def printkThFromEnd(self,k):
        if k>=self.getLength():
            print("K is Greater than the Linked List")
        else:
            k = self.getLength() - k - 1
            temp = self.head
            for i in range(k-1):
                temp = temp.next
            return temp.next.data
        


l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

ans = l1.printkThFromEnd(3)
print("Kth Node From End is : ",ans)