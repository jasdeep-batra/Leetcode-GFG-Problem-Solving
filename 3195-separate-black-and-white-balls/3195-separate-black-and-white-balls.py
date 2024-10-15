class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        ans = 0
        for item in s:
            if item=='1':
                black +=1
            elif item=='0':
                ans += black

        return ans


        