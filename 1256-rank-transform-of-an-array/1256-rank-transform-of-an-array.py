from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Sort the array but use a copy so as not to modify the original
        sarr = sorted(arr)
        mapp = {}
        count = 1

        # Assign ranks to elements in the sorted array, skipping duplicates
        for i in range(len(sarr)):
            if sarr[i] not in mapp:
                mapp[sarr[i]] = count
                count += 1

        # Map the ranks back to the original array
        result = [mapp[num] for num in arr]

        return result
