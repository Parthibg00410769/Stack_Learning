#Remember, for the stacks: Last IN First OUT
#checkout the note in the ONENOTE
#Whatever the last item is pushed will come out First

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        """Push the element at the last index"""
        self.items.append(item)
    def pop(self):
        """This will remove the last Item"""
        self.items.pop()

    def peek(self):
        """Allows to see the last element"""
        if self.items:
            return self.items[-1]
        else:
            return None
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None
    def isempty(self):
        """Tells whether the stack is Empty or not in Boolean"""
        if self.items == []:
            return True
        else:
            return False
stack = Stack()
stack.push("1")
stack.push("2")
stack.push("3")
print(stack.size())
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.size())