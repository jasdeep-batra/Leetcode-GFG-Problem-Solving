class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for item in s:
            if not stack:
                stack.append(item)
            elif item=='(':
                stack.append(item)
            
            elif item==')':
                if stack[-1]=='(':
                    stack.pop() 
                else:
                    stack.append(item)

        return len(stack)