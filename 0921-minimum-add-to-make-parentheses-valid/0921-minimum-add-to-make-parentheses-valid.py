class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for item in s:
            if not stack:
                stack.append(item)
            if item=='(':
                stack.append(item)
            
            if item==')':
                if stack[-1]=='(':
                    stack.pop() 
                else:
                    stack.append(item)

        return len(stack)