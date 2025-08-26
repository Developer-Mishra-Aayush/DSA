"""
Title: Merge Sort on Linked List
Approach: Split list at middle using slow/fast pointers, recursively sort halves, and merge two sorted lists.
Time: O(n log n)
Space: O(log n) recursion
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

    def merge(self,first,second):
        if first is None:
            return second
        if second is None:
            return None
        else:
            temp = Node(-1)
            realAns = temp
            while first and second:
                if first.val<=second.val:
                    temp.next = first
                    temp = first
                    first = first.next
                else:
                    temp.next = second
                    temp = second
                    second = second.next
            if first:
                temp.next = first
            if second:
                temp.next = second
            return realAns.next

    def getMiddle(self,head):
        if head is None or head.next is None:
            return head
        else:
            slow = head
            fast = head
            while fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                    slow = slow.next
            return slow


    def mergeSort(self,head):
        if head is None or head.next is None:
            return head
        else:
            mid = self.getMiddle(head)
            first = head
            second = mid.next
            mid.next = None
            first = self.mergeSort(first)
            second = self.mergeSort(second)
            ans = self.merge(first,second)
            return ans


l1 = LinkedList()
l1.head = Node(4)
second = Node(2)
third = Node(1)
fourth = Node(3)

l1.head.next = second
second.next = third
third.next = fourth

l1.Print(l1.head)
ans = l1.mergeSort(l1.head)
l1.Print(ans)