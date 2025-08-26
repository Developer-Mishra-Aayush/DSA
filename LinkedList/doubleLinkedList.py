class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def doubleIt(self, head):
        if head is None:
            return None
        else:
            totalNum = 0
            temp = head
            while temp:
                totalNum = totalNum*10 + temp.val
                temp = temp.next
            
            temp = head
            totalNum = totalNum*2
            totalNum = str(totalNum)
            i = 0
            while i<len(totalNum):
                if temp.next is None and i<len(totalNum):
                    newNode = Node(val = 9999)
                    temp.val = int(totalNum[i])
                    temp.next = newNode
                    temp = newNode
                    i+=1
                else:
                    temp.val = int(totalNum[i])
                    temp = temp.next
                    i+=1
            tempi = head
            while tempi.next:
                if tempi.next.val ==9999:
                    tempi.next = None
                else:
                    tempi = tempi.next
            return head
    def Print(self,head):
        temp = head
        while temp:
            print(temp.val,"->",end="")
            temp = temp.next
        print()
        
l1 = LinkedList()
l1.head = Node(9)
second = Node(9)
third = Node(9)

l1.head.next = second
second.next = third
ans = l1.doubleIt(l1.head)
l1.Print(ans)