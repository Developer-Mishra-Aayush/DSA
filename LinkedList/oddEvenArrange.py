"""
Title: Odd Even Linked List
Approach: Maintain odd and even pointers; relink nodes in one pass and attach even list after odd list.
Time: O(n)
Space: O(1)
"""

class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def oddEvenList(self,head):
        if head is None or head.next is None:
            return head
        else:
            odd = head
            even = head.next
            even_head = even

            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = even_head
            return head
    
        
    def Print(self,head):
        temp = head
        while temp:
            print(temp.data,"->",end="")
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
ans = l1.oddEvenList(l1.head)
l1.Print(ans)

# 1 -> 2 -> 3 -> 4 -> 5