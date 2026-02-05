class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        p = 0
        ans = 0
        for i,item in enumerate(s):
            if item=='(':
                stack.append(s)
            else:                
                if s[i-1]==')':
                    stack.pop()
                    continue                
                p = len(stack)-1
                ans+=2**p
                stack.pop()

        return ans
