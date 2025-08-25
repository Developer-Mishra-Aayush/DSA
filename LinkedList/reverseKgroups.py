class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLength(self,head):
        i =0
        temp = head
        while temp:
            i+=1
            temp = temp.next
        return i

    def reverseKGroups(self,head,k):
        if head is None or head.next is None:
            return head
        
        if k>self.getLength(head):
            print(" K is Greater as Comapred to Linked List ")
            return head
        
        prev = None
        curr = head
        forward = curr.next
        position =0

        while position < k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            position+=1
        if curr is not None:
            recursionHead = self.reverseKGroups(curr,k)
            head.next = recursionHead

        return prev
    
    def Print(self,head):
        temp = head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print()
    
l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

newHead = l1.reverseKGroups(l1.head,2)
l1.Print(newHead)