class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def _init__(self):
        self.head = None
        self.tail = None

    def mergeNodes(self,head):
        if head is None or head.next is None:
            return 0
        else:
            newhead = Node(-1)
            finalAns = newhead
            temp = head.next
            while temp:
                sum = 0
                while temp.val!=0:
                    sum+=temp.val
                    temp = temp.next
                if sum!=0:
                    newNode = Node(sum)
                    newhead.next = newNode
                    newhead = newNode
                temp = temp.next
            return finalAns.next
        
    def Print(self,head):
        temp = head
        while temp:
            print(temp.val,"->",end="")
            temp = temp.next
        print("NULL")

l1 = LinkedList()
l1.head = Node(0)
second = Node(3)
third = Node(1)
fourth = Node(0)
fifth = Node(4)
sixth = Node(5)
seventh = Node(2)
eight = Node(0)

l1.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = eight
ans = l1.mergeNodes(l1.head)
l1.Print(ans)