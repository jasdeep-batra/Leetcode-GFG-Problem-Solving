class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        summ = sum(nums)
        if summ%k!=0:
            return False
        target = summ//k
        visit = [0]*n
        memo = {}
        def recursion(i,k,s):
            #base case
            #exit condition
            if k==1:
                return True
            if (s)==target:
                return recursion(0,k-1,0)
            key = 0
            for ip in range(len(visit)):
                if visit[ip]:
                    key|=(1<<ip)
            if (key,k,s) in memo:
                return memo[(key,k,s)]
            for ind in range(i,n):
                if visit[ind]==1:
                    continue
                elif (s+nums[ind])<=target:
                    visit[ind] = 1
                    if recursion(ind+1,k,s+nums[ind]):
                        memo[(key,k,s)] = True
                        return True
                    visit[ind] = 0

            memo[(key,k,s)] = False
            return False

        return recursion(0,k,0)

