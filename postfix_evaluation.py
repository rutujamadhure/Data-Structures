#postfix evaluation

#create node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#define functions push and pop        
class Stack:
    def __init__(self):
        self.root=None
        
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.root
        self.root=new_node
    
    def pop(self):
        if self.root!=None:
            temp=self.root
            value=temp.data
            self.root=self.root.next
            del temp
            return value
            

s=input()
a=Stack()
for x in s:
    if x.isdigit():
        #push operand into stack
        a.push(x)
    else:
        #first pop will give second operand since stack is LIFO
        o2=a.pop()
        o1=a.pop()
        a.push(str(eval(o1+x+o2)))
print(int(float(a.pop())))       
            
    
