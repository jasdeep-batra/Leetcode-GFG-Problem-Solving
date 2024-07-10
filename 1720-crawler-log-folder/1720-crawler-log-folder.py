class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log=="./":
                continue
            if log=="../":
                if len(stack)==0:
                    continue
                else:
                    stack.pop(0)
            else:
                stack.append(log)

        return len(stack)
        
        