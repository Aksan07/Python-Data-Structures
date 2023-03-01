from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
def reverse_string(string):
    s=Stack()
    length=len(string)
    for i in range(length):
        s.push(string[i])
    str_reverse=" "
    for i in range(length):
        str_reverse+=s.pop()
    print(str_reverse)
reverse_string("We will conquere COVI-19")

    