class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if max_reach >= len(nums)-1:
                return True
            if max_reach >= i:
                max_reach  = max(max_reach,i+nums[i])
            else:
                return False
        return True


        
        