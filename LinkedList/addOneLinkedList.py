class Node:
    def __init__(self,data = 0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def reverseNode(self):
        if self.head == None:
            return self.head
        else:
            prev = None
            curr = self.head
            forward = curr.next
            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
            return prev
    def addOne(self):
        carry = 1
        self.head = self.reverseNode()
        temp  = self.head
        while temp.next:
            ans = temp.data + carry
            if ans >9:
                temp.data = ans-10
                carry = ans%10
            else:
                temp.data = ans
                carry = 0
            temp = temp.next
        if carry:
            newNode = Node(carry)
            temp.next = newNode
            self.tail = newNode
        self.head = self.reverseNode()

    def Print(self):
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print()


l1 = LinkedList()
l1.head = Node(4)
second = Node(5)
third = Node(6)

l1.head.next = second
second.next = third

l1.addOne()
l1.Print()