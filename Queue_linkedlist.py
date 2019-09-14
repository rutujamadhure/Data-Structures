class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isEmpty(self):
        return True if (self.front==None and self.rear==None) else False
           
    def enqueue(self,data): #insert at rear
        new_node=Node(data)
        if self.rear==None:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
            
    def dequeue(self):   #delete from front
        if self.isEmpty(): #Empty queue
            print('Queue is empty')
            return None
        else:
            value=self.front.data
            if self.front==self.rear: #For the case of only 1 node in queue
                self.front=self.rear=None
            else:
                self.front=self.front.next
            return value               

    def traverse(self):
         if self.isEmpty():
             print('Queue is empty')
         else:
             temp=self.front
             while temp!=self.rear:
                 print(temp.data,end=' ')
                 temp=temp.next
             print(self.rear.data)    
#test
Q=Queue()
Q.enqueue(5)
Q.enqueue(7)
Q.enqueue(2)
Q.dequeue()
Q.traverse()


            
        
