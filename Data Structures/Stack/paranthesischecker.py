from collections import deque

class Stack:
    def __init__(self):
        self.stack=deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
def is_balanced(string):
    balanced=False
    s=Stack()
    length=len(string)
    for i in range(length):
        s.push(string[i])
    str_reverse=[]
    for i in range(length):
        str_reverse.append(s.pop())
    if '('  in str_reverse:
        if ')' in str_reverse:
            balanced=True
        else:
            balanced=False
    elif ')' in str_reverse:
        if '(' in str_reverse:
            balanced=True
        else:
            balanced= False
    if '{'  in str_reverse:
        if '}' in str_reverse:
            balanced=True
        else:
            balanced=False
    elif '}' in str_reverse:
        if '{' in str_reverse:
            balanced=True
        else:
            balanced= False
    if '['  in str_reverse:
        if ']' in str_reverse:
            balanced=True
        else:
            balanced=False
    elif ']' in str_reverse:
        if '[' in str_reverse:
            balanced=True
        else:
            balanced= False
    print(balanced)
    
   
is_balanced("))")  