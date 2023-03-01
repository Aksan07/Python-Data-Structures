from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
s=Stack()
#PUSH OPERATION
s.push(5)
s.push(55)
print(s.stack)
#PEEK OPERATION
print(s.peek())
#POP OPERARTION
s.pop()
s.pop()
print(s.stack)
#IS EMPTY
print(s.is_empty())





