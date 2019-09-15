#Circular Queue using Linked List
#self.front points to the first node and self.rear points to the last node.(so, self.rear.next=self.front) The last node has the address of first node stored in 'next'.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_queue:
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue(self,data):
        if self.front==self.rear==None:
            self.front=self.rear=Node(data)

        else:   #insert at rear end
            new_node=Node(data)
            new_node.next=self.rear.next  #or new_node.next=self.front
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        if self.front==self.rear==None:
            print('Queue is empty')
            return None
        value=self.front.data
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            self.rear.next=self.front.next
            self.front=self.front.next
        return value
    def traverse(self):
        if self.front==self.rear==None:
            print('queue is empty')
            return None
        elif self.front==self.rear:
            print(self.front.data)
        else:
            temp=self.front
            while True:
                print(temp.data,end=" ")
                temp=temp.next
                if temp==self.front:
                    break

Q=Circular_queue()
Q.enqueue(4)
Q.enqueue(8)
Q.enqueue(3)
Q.enqueue(9)
Q.dequeue()
Q.traverse()



            
             
            
        
