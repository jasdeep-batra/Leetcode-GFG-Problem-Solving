class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for item in s:
            if item.isdigit():
                if not stack:
                    stack.append(item)
                elif stack[-1].isdigit():
                    stack[-1]+=item
                else:
                    stack.append(item)
            elif item =='[':
                stack.append(item)
            elif item !=']':
                if stack and stack[-1]!='[':
                    stack[-1]+=item
                else:
                    stack.append(item)

            elif item==']':
                print(stack)
                char = ""
                while stack[-1]!='[':
                    char = stack.pop() + char
                stack.pop()
                dig = stack.pop()
                ans = (char)*int(dig)
                stack.append(ans)
                
        print(stack)
        return "".join(stack)



