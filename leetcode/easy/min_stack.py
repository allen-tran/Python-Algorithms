class MinStack:
    
    def __init__(self):
        self.myStack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.myStack.append(val)
        if not self.minStack:
            minVal = val
        else:    
            minVal = min(val, self.minStack[-1])
        self.minStack.append(minVal)
        
    def pop(self):
        if self.myStack is None:
            return "Empty"
        else:
            self.myStack.pop()
            self.minStack.pop()
            
    def top(self):
        if self.myStack is None:
            return "Empty"
        else:
            return self.myStack[-1]

    def getMin(self):
        if self.minStack is None:
            return "Empty"
        else:
            return self.minStack[-1]