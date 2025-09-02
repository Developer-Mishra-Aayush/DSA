"""
Title: Min Stack
Approach: Maintain a data stack and a min stack that tracks the current minimum at each push
Time: O(1) per operation (push/pop/top/getMin)
Space: O(n)
"""

class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.data:
            popped = self.data.pop()
            if self.min_stack and self.min_stack[-1]==popped:
                self.min_stack.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            return -1

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()