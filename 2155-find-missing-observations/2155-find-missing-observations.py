class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = mean*(n+len(rolls))
        sumM = sum(rolls)
        sumN = total_sum - sumM

        if sumN < n or 6*n < sumN:
            return []
        
        avg = sumN//n
        rem = sumN%n

        result = [avg]*n

        for i in range(rem):
            result[i]+=1

        return result
        