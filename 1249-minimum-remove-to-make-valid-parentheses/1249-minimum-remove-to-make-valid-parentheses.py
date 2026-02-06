class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i,char in enumerate(s):
            if not stack and char in {'(',')'}:
                stack.append((i,char))

            elif char==')' and stack[-1][1]=='(':
                stack.pop()
            elif char in {'(',')'}:
                stack.append((i,char))

        ans = ""
        sett = set()
        for i,j in stack:
            sett.add(i)

        for i,c in enumerate(s):
            if i not in sett:
                ans+=c
        return ans

        return ""


            

