class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for item in s:
            if stack and item!=stack[-1] and (item.lower()==stack[-1].lower()):
                stack.pop()
            else:
                stack.append(item)

        return "".join(stack)
