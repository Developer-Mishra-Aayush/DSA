class Node:
    def __init__(self,data = 0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def nodesBetweenCriticalPoints(self, head):
        if head is None or head.next is None:
            return []
        else:
            firstCp = -1
            lastCp = -1
            currCp = -1
            localMaxima = -1
            localMinima = float('inf')

            i = 1
            prev = head
            curr = head.next
            forward = curr.next
            while forward is not None:
                forward = curr.next
                if ((curr.data>prev.data and curr.data>forward.data) or (curr.data<prev.data and curr.data<forward.data)):
                    if firstCp!=-1:
                        localMinima = min(localMinima,(i - lastCp))
                        print("local Minima is : ",localMinima)
                    else:
                        firstCp = i
                    lastCp = i
                i+=1
                prev = curr
                curr = forward
                forward = forward.next
            if firstCp ==-1 or lastCp==firstCp:
                return [-1,-1]
            if firstCp!=-1 and lastCp!=-1:
                localMaxima = lastCp - firstCp
        return [localMinima,localMaxima]
        