from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        
        # Count the occurrences of each remainder
        for num in arr:
            remainder = num % k
            # Handling negative remainders to make them positive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1
        
        # Now we check if pairs can be formed
        # 1. For remainder 0, there must be an even number of such elements
        if remainder_count[0] % 2 != 0:
            return False
        
        # 2. For other remainders, there must be a matching pair (remainder, k - remainder)
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True
