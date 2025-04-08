class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = [0]*101
        count = 0
        n = len(nums)
        for i in range(n-1,-1,-1):
            if arr[nums[i]]>0:
                rem = n-count
                return math.ceil(rem/3)
            else:
                arr[nums[i]]+=1
                count+=1
        return 0



        