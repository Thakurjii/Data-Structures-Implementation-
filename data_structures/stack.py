"""   Stack Implementation from list   """


class Stack(object):
    """   Represents a Stack   """
    def __init__(self):
        self.stack = []

    # returns True if the stack is empty
    def is_empty(self):
        return self.stack == []

    # inserts data onto the stack
    def push(self, data):
        self.stack.append(data)
    
    # removes and returns the top element of the stack
    def pop(self):
        top = self.stack[-1]
        del self.stack[-1]
        return top
    
    # returns the top element of the stack
    def peek(self):
        return self.stack[-1]
    

if __name__ == '__main__':
    stack1 = Stack()
    print('Stack is empty :', stack1.is_empty())
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    print('Stack is empty :', stack1.is_empty())
    print(stack1.pop())
    print(stack1.peek())

