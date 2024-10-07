class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for item in s:
            if len(stack)>0 and item=='B' and stack[-1]=='A':
                stack.pop()
            elif len(stack)>0 and  item=='D' and stack[-1]=='C':
                stack.pop()
            else:
                stack.append(item)
        return len(stack)

        