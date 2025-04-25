from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        prefix = 0
        result = 0

        count[0] = 1  # Start with 0 prefix count

        for num in nums:
            if num % modulo == k:
                prefix += 1
            # Use modulo to normalize the value
            result += count[(prefix - k) % modulo]
            count[prefix % modulo] += 1

        return result
