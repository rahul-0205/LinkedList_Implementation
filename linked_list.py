class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None
    def insert(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
def printl(head):
    temp=head
    while temp:
        print(temp.data,end=' ')
        temp=temp.next
ll=LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
printl(ll.head)
            
