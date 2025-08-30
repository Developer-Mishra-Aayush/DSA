class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_duplicate(self):
        if self.head is None or self.head.next is None:
            return self.head
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == temp.data and temp.next.next:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
    
    def Print(self):
        temp = self.head
        while temp:
            print(temp.data,"->",end="")
            temp = temp.next
        print()
        

l1 = LinkedList()
l1.head = Node(10)
second = Node(10)
third = Node(10)
fourth = Node(20)
fifth = Node(20)
sixth = Node(30)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
l1.remove_duplicate()
l1.Print()