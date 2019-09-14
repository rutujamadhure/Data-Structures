#For an input string of the form eg. "3[a3[b]1[ab]]" , write a code to display output as "abbbababbbababbbab". The code should take T(no. of test cases)as input.
#Example 2: input: 3[b2[ca]]
#          output:bcacabcacabcaca

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
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

    def peek(self):
         if self.root:
             return self.root.data
            
            
T=int(input())
dict1={'(':')','{':'}','[':']'}
stack=Stack()
for i in range(T):
    s=input()
    for x in s:
        if x not in dict1.values():    #if closing bracket does not appear, push element into stack
            stack.push(x)
        else:
            string=""   #to form substring
            while True:
                v=stack.pop()
                if ((v in dict1.keys()) and (dict1[v]==x)): #if closing bracket is popped, break
                    break
                else:
                    string=v+string
            times=""     #number of times the substring is repeated
            while True:
                if (not stack.root): #break out of the loop if stack is empty
                    break
                else:
                    if (not stack.peek().isdigit()):
                        break
                    else:   #append only if the element is a digit
                        times=stack.pop()+times
                                
            string=string*int(times)
            stack.push(string)
            
    print(stack.pop())        
            
            
            
        
        
