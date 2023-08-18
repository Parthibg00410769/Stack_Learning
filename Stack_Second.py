class Stack(object):
    def __init__(self):
        self.items = []
        self.top = None

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item1):
        self.items.append(item1)
        self.top = len(self.items) - 1

    def pop(self):
        if self.isEmpty():
            return "UnderFlow!!"
        else:
            i = self.items.pop()
            if len(self.items) == 0:
                self.top = None
            else:
                self.top = self.top - 1
        return i

    def peek(self):
        if self.isEmpty():
            return "UnderFlow!!"
        else:
            self.top = len(self.items) - 1
            return self.items[self.top]

    def display(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            self.top = len(self.items) - 1
            print(self.items[self.top], '<---Top')
            for i in range(self.top, -1, -1):
                print(self.items[i])
            print("Top: %d" % self.top)


stack = Stack()
while True:

    print("STACK IMPLEMENTATION PROGRAM!")
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display')
    print('5. Exit')
    ch = int(input("Enter the choice(1-5)"))
    if ch == 1:
        item = int(input("Enter the item you want to push: "))
        stack.push(item)
        print('%d added successfully' % item)
        input("Press any key to continue")

    elif ch == 2:
        item = stack.pop()
        if item == 'UnderFlow':
            print("Stack is empty")
        else:
            print('%d is popped' % item)
        input("Press any key to continue")

    elif ch == 3:
        item = stack.peek()
        if item == 'UnderFlow':
            print("Stack is empty")
        else:
            print('%d is at the top' % item)
        input("Press any key to continue")
    elif ch == 4:
        stack.display()
        input("Press any key to continue")
    elif ch == 5:
        break
    else:
        print("Please choose the right option")
