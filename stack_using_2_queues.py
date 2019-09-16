#Implement stack using 2 queues

#Queue data structure
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
q1=Queue()
q2=Queue()

#we will enqueue the data in q1. And insert elements from queue q2 into q1.
#Finally insert the elements from q1 into q2. Dequeue operation will be done using q2. This will act as last in first out.
def push_in_stack(q1,q2,data):
    q1.enqueue(data)
    while not q2.isEmpty():
        q1.enqueue(q2.dequeue())
    while not q1.isEmpty():
        q2.enqueue(q1.dequeue())

def pop_stack(q1,q2):
    if not q2.isEmpty():
        return q2.dequeue()

def traverse(q1,q2):
    if not q2.isEmpty():
        temp=q2.front
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
    else:
        print('stack is empty')
        

push_in_stack(q1,q2,3)
push_in_stack(q1,q2,8)
push_in_stack(q1,q2,9)
push_in_stack(q1,q2,6)
pop_stack(q1,q2)
traverse(q1,q2)
