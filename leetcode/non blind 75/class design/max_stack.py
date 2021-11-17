class MaxStack(object):

    def init(self):
        stack = []
        maxStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.maxStack:
            max_val = x
        else:
            max_val = max(x, self.maxStack[-1])
        self.maxStack.append(max_val)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return "Empty"
        else:
            self.max_stack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return "Empty"
        else:
            return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        if not self.max_stack:
            return "Empty"
        else:
            return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        if not self.max_stack:
            return "Empty"
        else:
            return self.max_stack[-1]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
