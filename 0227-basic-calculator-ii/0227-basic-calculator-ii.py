class Solution:
    def calculate(self, s: str) -> int:
        stack  = []
        sign = '+'
        dig = 0
        s+='+'
        for char in s:
            if char.isdigit():
                dig = 10*dig + int(char)
            elif char==" ":
                continue
            else:
                if sign=='/':
                    stack.append(int(stack.pop()/(dig)))
                elif sign=='*':
                    stack.append(stack.pop()*(dig))
                else:
                    pos = 1 if sign=='+' else -1
                    stack.append(pos*dig)
                sign=char
                dig = 0

        print(stack)
        return sum(stack)
