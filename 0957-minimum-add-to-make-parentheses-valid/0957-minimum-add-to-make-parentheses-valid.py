class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for item in s:
            if len(stack)==0:
                stack.append(item)
            elif item=='(':
                stack.append('(')
            elif item==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
                
        return len(stack)
            
        