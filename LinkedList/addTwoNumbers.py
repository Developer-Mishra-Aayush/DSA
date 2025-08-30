"""
Title: Add Two Numbers (Linked Lists)
Approach: Traverse both lists simultaneously, summing digits with carry, and build result via a dummy head.
Time: O(m + n)
Space: O(1) extra (excluding output list)
"""

class Node:
    def __init__(self,data=0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addTwo(self,h1,h2):
        if not h1.head and not h2.head:
            return None
        if not h1.head:
            return h2.head
        if not h2.head:
            return h1.head

        carry = 0
        temp1 = h1.head
        temp2 = h2.head
        ans = Node(-1)   # dummy node
        finalAns = ans

        while temp1 or temp2:
            val1 = temp1.data if temp1 else 0
            val2 = temp2.data if temp2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            newNode = Node(total % 10)
            ans.next = newNode
            ans = newNode

            if temp1: temp1 = temp1.next
            if temp2: temp2 = temp2.next

        if carry:
            ans.next = Node(carry)

        return finalAns.next
    
    def Print(self,head):
        temp = head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print("None")

# Example
h1 = LinkedList()
h2 = LinkedList()

h1.head = Node(2)
h1.head.next = Node(4)
h1.head.next.next = Node(3)   # number 342

h2.head = Node(5)
h2.head.next = Node(6)
h2.head.next.next = Node(4)   # number 465

ans = h1.addTwo(h1,h2)
h1.Print(ans)
