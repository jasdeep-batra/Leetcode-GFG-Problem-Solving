class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left,right = [-1]*n,[n]*n
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
            while stack and heights[stack[-1]] > heights[i]:
                right[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            if not stack:
                stack.append(i)
            while stack and heights[stack[-1]] > heights[i]:
                left[stack[-1]] = i
                stack.pop()
            stack.append(i)

        print(left)
        print(right)
        area = 0
        for i in range(n):
            area = max(area,heights[i]*(right[i]-left[i]-1))

        return area
