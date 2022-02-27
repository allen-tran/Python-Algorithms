class StackQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, number):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(number)

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            print('Queue is empty')
        
        return self.s1.pop()
