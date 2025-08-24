class Node:
    def __init__(self,data=0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Print(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp:
                print(temp.data," -> ",end="")
                temp = temp.next
            print()

    def reverseLinkedList(self):
        if self.head is None and self.head.next is None:
            return
        else:
            prev = None
            curr = self.head
            forward = curr.next

            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
            self.head = prev


    

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

l1.reverseLinkedList()
l1.Print()