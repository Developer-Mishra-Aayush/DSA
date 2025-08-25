class Node:
    def __init__(self,data = 0):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def mergeTwoLists(self,l1,l2):
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        else:
            ans = Node(-1)
            finalAns = ans

            while l1 and l2:
                if l1.data <=l2.data:
                    ans.next = l1
                    ans = l1
                    l1 = l1.next

                else:
                    ans.next = l2
                    ans = l2
                    l2 = l2.next
            while l1 is not None:
                ans.next = l1
                ans = l1
                l1 = l1.next
            while l2 is not None:
                ans.next = l2
                ans = l2
                l2 = l2.next
            return finalAns.next
        
    def Print(self,head):
        temp = self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp = temp.next
        print()
                


l1 = LinkedList()
l2 = LinkedList()

l1.head = Node(1)
second = Node(2)
third = Node(4)

l1.head.next = second
second.next = third

l2.head = Node(1)
second1 = Node(3)
third1 = Node(4)

l2.head.next = second1
second1.next = third1

ans = l1.mergeTwoLists(l1.head,l2.head)
l1.Print(ans)