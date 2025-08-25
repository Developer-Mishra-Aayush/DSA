class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLength(self):
        i = 0
        temp = self.head
        while temp:
            temp = temp.next
            i+=1
        return i
    
    def Print(self):
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print()

    def rotateList(self,k):
        if k == 0:
            return self.head
        else:
            k = k% self.getLength()
            requiredLength = self.getLength() - k
            i = 0
            temp = self.head
            while i<requiredLength-1:
                i+=1
                temp = temp.next
            tempi = temp.next
            temp.next = None
            finalHead = tempi
            while tempi.next:
                tempi = tempi.next
            tempi.next = self.head
            self.head = finalHead
            return self.head

    
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
ans = l1.rotateList(2)
l1.Print()