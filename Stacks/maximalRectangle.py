"""
Title: Maximal Rectangle in Binary Matrix
Approach: Treat each row as the base of a histogram by accumulating consecutive 1s column-wise; for each row, compute Largest Rectangle in Histogram using monotonic stacks (prev/next smaller) and take the maximum area across rows
Time: O(m*n) to build heights + O(m*n) for histograms = O(m*n)
Space: O(n) auxiliary for stacks per row
"""

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

    def maximalRectangle(self, matrix):
        int_matrix = []
        for row in matrix:
            int_row = [int(x) for x in row]
            int_matrix.append(int_row)
        
        area = self.largestRectangleArea(int_matrix[0])
        for i in range(1,len(int_matrix)):
            for j in range(len(matrix[0])):
                if int_matrix[i][j]:
                    int_matrix[i][j]+=int_matrix[i-1][j]
                else:
                    int_matrix[i][j]
            area = max(area,self.largestRectangleArea(int_matrix[i]))
        return area