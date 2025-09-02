"""
Title: Online Stock Span
Approach: Maintain a monotonic decreasing stack of (price, span); merge spans while popping <= price
Time: O(n) amortized
Space: O(n)
"""
from collections import deque
class StockSpanner(object):

    def __init__(self):
        self.stack = deque()

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0]<=price:
            span+=self.stack[-1][1]
            self.stack.pop()
        l = [price,span]
        self.stack.append(l)
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)