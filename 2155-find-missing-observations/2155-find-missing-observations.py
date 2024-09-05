class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Calculate the total sum needed for n missing rolls
        total_sum = mean * (len(rolls) + n)
        sumM = sum(rolls)
        sumN = total_sum - sumM
        
        # If sumN is negative or too large for n dice, return empty list
        if sumN < n or sumN > 6 * n:
            return []
        
        # Initialize the result with the minimum possible value
        result = [sumN // n] * n
        remainder = sumN % n
        
        # Distribute the remainder to ensure the total adds up to sumN
        for i in range(remainder):
            result[i] += 1
        
        return result
