class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        dictt= {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in dictt:
                dictt[nums[i]] = i
            if nums[i]-1 in dictt:
                ans = max(ans,i-dictt[nums[i]-1]+1)
        return ans
