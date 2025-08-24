class Node:
    def __init__(self,data=0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isCycle(self):
        if self.head is None or self.head.next is None:
            return False
        else:
            slow = self.head
            fast = self.head

            while fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                    slow = slow.next
                if fast==slow:
                    print("Coming here ")
                    print("Fast data : ",fast.data ,"ans slow data :",slow.data)
                    return True
            return False

l1 = LinkedList()
l1.head = Node(3)
second = Node(2)
third = Node(0)
fourth = Node(4)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = second
print("Is Cycle Present : ",l1.isCycle())