class Stack:
    def __init__(self):
        self.stack = []

    def add(self, number):
        self.stack.append(number)

    def pop(self):
        self.stack.pop()

    def __len__(self):
        return len(self.stack)
