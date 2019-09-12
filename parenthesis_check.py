#Parenthesis Checker

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

#Code for parenthesis check
a=Stack()
s=input('Enter string')
dict1={'(':')','{':'}','[':']'}
flag=True

for x in s:
    if x in dict1.keys():
        a.push(x)
    elif x in dict1.values():
        if a.isEmpty():
            flag=False
            break
        else:
            if dict1[a.peek()]==x:
                a.pop()
            else:
                flag=False
                break

#check if any unbalanced parenthesis is left in stack
            
if not a.isEmpty():
    flag==False

print('Balanced') if flag==True else print('Not balanced')
               
            
