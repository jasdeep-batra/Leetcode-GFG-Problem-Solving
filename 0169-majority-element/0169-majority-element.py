class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = 0
        count = 0
        for item in nums:
            if count==0:
                val = item
            if item==val:
                count+=1
            else:
                count-=1
        return val

        