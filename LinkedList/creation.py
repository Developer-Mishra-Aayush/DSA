class Node:
    def __init__(self,data=0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Print(self):
        temp = self.head
        while temp:
            print(temp.data,' ->',end= " ")
            temp = temp.next
        print()

    def insertAthead(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtTail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
    def insertAtIndex(self,data,index):
        print("Insert At index Is Called ")
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            print("Insert At index Is Called 2")
            temp = self.head
            i = 0
            while i<index-1 and temp.next is not None:
                i+=1
                print("i is : ",i)
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

            if newNode.next is None:
                self.tail = newNode

    def deleteAtHead(self):
        if not self.head:
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None

    def deleteAtTail(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            self.tail = temp
            temp.next = None

l1 = LinkedList()
l1.insertAthead(1)
l1.insertAthead(2)
l1.insertAtIndex(3,3)

l1.insertAtTail(4)
l1.insertAtTail(5)

l1.deleteAtHead()
l1.deleteAtTail()

l1.Print()