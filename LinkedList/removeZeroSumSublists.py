"""
Title: Remove Zero Sum Consecutive Nodes from Linked List
Approach: Use prefix sums with a map from sum to node; first pass records last occurrence, second pass relinks to skip zero-sum ranges.
Time: O(n)
Space: O(n)
"""

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def Print(self,head):
        temp = head
        while temp:
            print(temp.val,"->",end="")
            temp = temp.next
        print()

    def removeZeroSumSublists(self,head):
        dummy = Node(0)
        dummy.next = head
        prefix_sum = 0
        seen = {}

        curr = dummy
        while curr:
            prefix_sum+=curr.val
            seen[prefix_sum] = curr
            curr = curr.next
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum+=curr.val
            curr.next = seen[prefix_sum].next
            curr = curr.next
        return head

l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(-3)
fifth = Node(4)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
ans = l1.removeZeroSumSublists(l1.head)
l1.Print(ans)