class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #evaluare then push it into the stack
        stack = []
        def calc(a,b,op):
            if op=="+":
                return a+b
            if op=="-":
                return a-b
            if op=="*":
                return a*b
            return int(a/b)
        special = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in special:
                stack.append(token)
            
            if token in special:
                num2,num1 = int(stack.pop()),int(stack.pop())
                num3 = str(calc(num1,num2,token))
                print(num1," ",num2," ",num3)
                stack.append(num3)

        return int(stack[-1])


                