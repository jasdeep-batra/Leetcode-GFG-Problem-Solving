from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq_set = set()  # To track seen elements
        res = []          # Result array
        common_count = 0  # Count of common elements so far
        
        for i in range(len(A)):
            # Check and update for A[i]
            if A[i] in freq_set:
                common_count += 1
            freq_set.add(A[i])
            
            # Check and update for B[i]
            if B[i] in freq_set:
                common_count += 1
            freq_set.add(B[i])
            
            # Append the current common count to the result
            res.append(common_count)
        
        return res
