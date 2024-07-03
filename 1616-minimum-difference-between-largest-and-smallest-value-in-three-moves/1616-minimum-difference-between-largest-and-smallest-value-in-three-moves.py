class Solution:
    def minDifference(self, nums: List[int]) -> int:
        #binary search
        nums.sort()
        i = 0
        j = len(nums)-1
        # j-3 i+3  i+2 j-2 j-1 i+1
        ans3 = sys.maxsize
        if(len(nums)<=3):
            return 0
        ans1 = min((nums[j-3]-nums[i]), (nums[j]-nums[i+3]))
        ans2 = min((nums[j-2]-nums[i+1]), (nums[j-1]-nums[i+2]))
        ans3 = min(ans1,ans2)
        return ans3


        