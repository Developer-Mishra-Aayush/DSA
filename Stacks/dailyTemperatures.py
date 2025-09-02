from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0 for _ in range(len(temperatures))]
        stack = deque()
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                stack.append(i)
            elif stack and temperatures[stack[-1]]<=temperatures[i]:
                while stack and temperatures[stack[-1]]<=temperatures[i]:
                    stack.pop()
                if stack and temperatures[stack[-1]]>temperatures[i]:
                    ans[i] = stack[-1] - i
                stack.append(i)
            elif stack and temperatures[stack[-1]]>temperatures[i]:
                ans[i] = stack[-1] - i
                # stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        return ans