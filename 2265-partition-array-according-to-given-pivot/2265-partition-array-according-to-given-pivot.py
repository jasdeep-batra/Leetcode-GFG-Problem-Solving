class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [item for item in nums if item < pivot] + [item for item in nums if item==pivot]+ [item for item in nums if item > pivot]
            


        