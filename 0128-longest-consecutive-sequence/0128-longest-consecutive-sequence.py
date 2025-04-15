class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        count = 0
        res = 0
        for item in nums:
            if item-1 not in nums:
                j = item+1
                while j in nums:
                    j+=1
                
                res = max(res,j-item)
        return res

