class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s=list(s)
        for i,char in enumerate(s):
            if not stack and char in {'(',')'}:
                stack.append((i,char))

            elif char==')' and stack[-1][1]=='(':
                stack.pop()
            elif char in {'(',')'}:
                stack.append((i,char))

        ans = ""

        while stack:
            s[stack.pop()[0]]=""

        return "".join(s)


            

