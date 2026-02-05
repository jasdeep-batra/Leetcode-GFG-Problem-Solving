class Solution:
    def calculate(self, s: str) -> int:
        #we need to take care of bodmas
        def solve(a,b,o):
            if o=='-':
                return a-b
            else:
                return a+b
        stack = []
        op = {'-','+'}
        neg =  False
        for c in s:
            if c.isdigit():
                if stack and stack[-1][-1].isdigit():
                    stack[-1]+=c
                else:
                    if stack and stack[-1]=='-':
                        stack.pop()
                        stack.append('-'+c)
                    else:
                        stack.append(c)
                
                
                    
            if c=='+' or c=='-' or c=='(':
                stack.append(c)
            elif c==')':
                ans = 0
                while stack[-1]!='(':
                    curr = stack.pop()
                    if curr[-1].isdigit():
                        ans+=int(curr)                
                stack.pop()
                if stack and stack[-1]=='-':
                    stack.pop()
                    if str(ans)[0]!='-':
                        stack.append('-'+str(ans))
                    else:
                        stack.append(str(ans)[1:])
                else:
                    stack.append(str(ans))
            # print(stack)

        ans = 0
        # print(stack)
        while stack:
            curr = stack.pop(0)
            if curr[-1].isdigit():
                ans+=int(curr)


        return ans
                
                
                        
                    
                
                

