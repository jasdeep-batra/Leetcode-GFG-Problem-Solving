class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #problem of range addition in which we add or subtract among the range
        # then later on we decide weather it has incremtn or decremnt
        #how we use to o t

        helper = [0]*(len(nums)+1)
        for l,r in queries:
            helper[l]+=1
            helper[r+1]-=1

        reduce = 0
        for i in range(len(helper)-1):
            if helper[i]:
                reduce+=helper[i]
            nums[i]-=reduce
        print(nums)
        for item in nums:
            if item > 0:
                return False
        return True




        
        