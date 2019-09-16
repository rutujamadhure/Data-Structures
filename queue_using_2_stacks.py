#queue using 2 stacks

class Stack:
    def __init__(self):
        self.array=[]
        self.top=-1
        
    def push(self,data):
        self.array.append(data)
        self.top=self.top+1

    def pop(self):
        if self.top==-1:
            return None
        else:
            value=self.array.pop(self.top)
            self.top=self.top-1
            return value
    def traverse_stack(self):
        for i in range(self.top+1):
            print(self.array[i],end=' ')
            
s1=Stack()
s2=Stack()

def enqueue(data):
    s1.push(data)

def dequeue():
    if s1.top!=-1:
        while s1.top!=-1:
            s2.push(s1.pop())
        value=s2.pop()
        print(value)
        while s2.top!=-1:
            s1.push(s2.pop())
        return value
    else:
        return None

def traverse():
    if s1.top==-1:
        return None
    else:
        s1.traverse_stack()
        
        
enqueue(2)
enqueue(1)
enqueue(3)
enqueue(9)
dequeue()
traverse()

            
