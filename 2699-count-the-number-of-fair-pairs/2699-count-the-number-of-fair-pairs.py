class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upp: int) -> int:
        # is it  a subproblem of two sum problem
        nums.sort()
        #binary sort ?
        
        def helper(upper):
            i = 0
            j = len(nums)-1
            res = 0
            while( i<j):
                if (nums[j]+nums[i]) > upper:
                    j-=1
                else:
                    res+=(j-i)
                    i+=1
            return res

        return helper(upp)-helper(lower-1)
            

            
        