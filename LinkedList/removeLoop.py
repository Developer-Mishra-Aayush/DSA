class Node:
    def __init__(self,data=0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def detectCycle(self):
        if self.head is None or self.head.next is None:
            return self.head
        else:
            slow = self.head
            fast = self.head
            while fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                    slow = slow.next
                if fast==slow:
                    print("Slow is : ",slow.data)
                    slow = self.head
                    forward = Node(-1)
                    forward.next = fast
                    while slow!=fast:
                        forward = forward.next
                        fast = fast.next
                        slow = slow.next
                    forward.next = None
                    return self.head
    def Print(self):
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print()


l1 = LinkedList()
l1.head = Node(3)
second = Node(2)
third = Node(0)
fourth = Node(-4)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = second
ans = l1.detectCycle()

l1.Print()
print("Staring point of a Linked List is : ",ans.data)