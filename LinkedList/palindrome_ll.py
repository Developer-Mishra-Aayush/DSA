class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getMiddle(self):
        if self.head is None:
            print("Empty LL")
        elif self.head.next is None:
            return self.head
        else:
            slow = self.head
            fast = self.head
            while fast.next:
                fast = fast.next
                if fast.next:
                    fast = fast.next
                    slow = slow.next
            return slow
        
    def reverseNode(sself,head):
        if head is None or head.next is None:
            return head
        else:
            curr = head
            prev = None
            forward = curr.next
            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
            head = prev
            return head
        
    def palindromeLinkedList(self):
        if self.head is None or self.head.next is None:
            return self.head
        else:
            slow = self.head
            fast = self.head
            while fast.next:
                fast = fast.next
                if fast.next:
                    slow = slow.next
                    fast = fast.next
            second = None
            first = self.head
            second = self.reverseNode(slow.next)

            while second:
                if first.data != second.data:
                    return False
                first = first.next
                second = second.next
            return True
    
l1 = LinkedList()
l1.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(20)
fifth = Node(10)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print("Is Palindrome Linked List :",l1.palindromeLinkedList())