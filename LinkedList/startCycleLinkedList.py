"""
Title: Start of Cycle in Linked List
Approach: Detect cycle with Floyd; reset one pointer to head and move both one step to find cycle entry.
Time: O(n)
Space: O(1)
"""

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
                    while slow!=fast:
                        fast = fast.next
                        slow = slow.next
                    return slow


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
print("Staring point of a Linked List is : ",ans.data)