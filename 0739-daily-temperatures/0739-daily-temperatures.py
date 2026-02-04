class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                res[stack.pop()] = i

            stack.append(i)

        for i in range(len(res)):
            res[i] = res[i] - i if res[i]!=0 else 0

        return res