#Queue without linked list in python

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.array=[]

    def isEmpty(self):
        if self.front==self.rear==None:
            return True
        else:
            return False
    def enqueue(self,data):
        if self.isEmpty():
            self.front=self.rear=0
        else:
            self.rear=self.rear+1
        self.array.append(data)

    def dequeue(self):
        if self.isEmpty():
            return None
        elif self.front==self.rear==0:
            value=self.array[self.front]
            self.front==self.rear==None
        else:
            value=self.array[self.front]
            self.front=self.front+1
        return value
    
    def traverse(self):
        if not self.isEmpty():
            temp=self.front
            while temp!=self.rear:
                print(self.array[temp],end=' ')
                temp=temp+1
            print(self.array[self.rear])    

q=Queue()
q.enqueue(2)
q.enqueue(9)
q.enqueue(6)
q.dequeue()
q.traverse()
