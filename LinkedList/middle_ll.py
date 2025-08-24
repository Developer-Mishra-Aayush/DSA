class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Middle(self):
        if not self.head:
            return
        elif self.head.next == None:
            return self.head.data
        else:
            slow = self.head
            fast = self.head
            while fast.next:
                fast = fast.next
                if fast.next is not None:
                    slow = slow.next
                    fast = fast.next
            return slow.data

l1 = LinkedList()
l1.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Middle Element in A Linked List is : ",l1.Middle())
        