class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack)>=len(part):
                if part in "".join(stack):
                    for i in range(len(part)):
                        stack.pop()

        return "".join(stack)
            


        