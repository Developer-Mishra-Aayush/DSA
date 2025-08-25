class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def modify(self,head,m,n):
        if head is None:
            return None
        
        # Skip M Nodes in LinkedList
        curr = head
        for i in range(1,m):
            if curr is None:
                return head
            curr = curr.next
        if curr is None:
            return head
        
        # Delete N Nodes In Linked List
        temp = curr.next
        for i in range(n):
            if temp is None:
                break
            temp = temp.next
        curr.next = temp
        curr = temp
        self.modify(curr,m,n)
        return head
    
    def Print(self, head):
        temp = head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------- Example ----------------
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)
ll.head.next.next.next.next.next = Node(6)
ll.head.next.next.next.next.next.next = Node(7)
ll.head.next.next.next.next.next.next.next = Node(8)

print("Original List:")
ll.Print(ll.head)

ll.head = ll.modify(ll.head, m=2, n=2)  # Keep 2, delete 2
print("\nModified List (keep 2, delete 2):")
ll.Print(ll.head)
       