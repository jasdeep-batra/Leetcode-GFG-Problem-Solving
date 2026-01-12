class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_area(pipe_var):
            stack = []
            area = 0
            i = 0
            while i < len(pipe_var):
                if not stack or pipe_var[i] > pipe_var[stack[-1]]:
                    stack.append(i)
                    i+=1
                else:
                    height = pipe_var[stack.pop()] #stack top element
                    j = stack[-1] if stack else -1
                    area = max(area,height*(i-j-1))

            while stack:
                height = pipe_var[stack.pop()]
                j = stack[-1] if stack else -1
                area = max(area,height*(i-j-1))

            return area
                    
        pipe = [0 for i in range(len(matrix[0]))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    pipe[j]+=1
                else:
                    pipe[j] = 0
            res = max(res,get_area(pipe))
        return res
