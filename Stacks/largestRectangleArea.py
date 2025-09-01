class Solution:
    def prev_smaller(self,heights):
        ans = [0 for _ in range(len(heights))]
        stack = []
        stack.append(-1)
        for i in range(0,len(heights)):
            currElement = heights[i]
            while stack[-1]!=-1 and heights[stack[-1]]>=currElement:
                stack.pop()
            ans[i] = stack[-1]

            stack.append(i)
        return ans

    def nextSmallerElement(self,heights):
        ans = [0 for _ in range(len(heights))]
        stack = []
        stack.append(-1)

        for i in range(len(heights)-1,-1,-1):
            currElement = heights[i]
            while stack[-1]!=-1 and heights[stack[-1]]>=currElement:
                stack.pop()
            ans[i] = stack[-1]
            stack.append(i)
        for i in range(len(ans)):
            if ans[i]==-1:
                ans[i]=len(heights)
        return ans

    def largestRectangleArea(self, heights):
        prev = self.prev_smaller(heights)
        next = self.nextSmallerElement(heights)
        ans = -2**32
        for i in range(len(heights)):
            width = next[i] - prev[i] - 1
            height = heights[i]
            area = width*height
            ans = max(ans,area)
        return ans