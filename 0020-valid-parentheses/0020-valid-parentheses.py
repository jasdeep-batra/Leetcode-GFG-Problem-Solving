class Solution:
    def isValid(self, s: str) -> bool:
        o,c = 0,0
        stack = []
        for char in s:
            if char in ('(','{','['):
                stack.append(char)
            elif stack:
                if char==')' and stack[-1]!='(':
                    return False
                if char==']' and stack[-1]!='[':
                    return False
                elif char=='}' and stack[-1]!='{':
                    return False
                stack.pop()
            else:
                return False

        return True if not stack else False