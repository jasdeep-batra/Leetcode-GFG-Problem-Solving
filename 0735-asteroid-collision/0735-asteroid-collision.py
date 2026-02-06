class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            ast = asteroids[i]
            if stack and ast <= 0 and stack[-1]>=0:
                if stack[-1]==-ast:
                    stack.pop()
                    i+=1
                    continue
                elif stack[-1] > -ast:
                    i+=1
                    continue
                elif (stack[-1] > 0) and (stack[-1] < -ast):
                    stack.pop()
            else:
                stack.append(ast)
                i+=1

        return stack
                

                
