class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left,right = [-1]*n,[n]*n
        stack = []
        area = 0
        heights.append(0)
        for i in range(n+1):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1] -1 
                area = max(area,height*width)
            stack.append(i)
        return area
