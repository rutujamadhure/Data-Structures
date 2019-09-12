#Python Implementation of Stack using Linked List

#create stack node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#root stores address of first node
class Stack:
    def __init__(self):
        self.root=None

    def isEmpty(self):
        return True if self.root==None else False

#insert element at the beginning/start
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.root
        self.root=new_node

#remove first element present at the beginning
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            temp=self.root
            value=temp.data
            self.root=self.root.next
            del temp
            return value

#return element present at the beginning
    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            return self.root.data

#traverse through elements of stack
    def traverse(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            temp=self.root
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
            
                
#Test code        

a=Stack()
a.push(5)
a.push(10)
a.push(3)
a.pop()
a.peek()
a.traverse()
