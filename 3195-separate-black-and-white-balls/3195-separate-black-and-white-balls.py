class Solution:
    def minimumSteps(self, s: str) -> int:
        stack = []
        ans = 0
        for item in s:
            if not stack and item=='1':
                stack.append(item)
            elif item=='0':
                ans += len(stack)
            elif item=='1':
                stack.append('1')

        return ans


        