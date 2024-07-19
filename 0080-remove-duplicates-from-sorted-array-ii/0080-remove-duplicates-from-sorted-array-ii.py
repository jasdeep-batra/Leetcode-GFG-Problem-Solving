class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # map
        replace = -sys.maxsize-1
        i,j = 0,1
        k = 0
        while(j<len(nums)):
            if nums[j]==nums[i]:
                if j-i+1 > 2:
                    nums[j] = replace   
                    k+=1
                              
            else:
                i=j
            j+=1

        kk = len(nums)-k
        h = 0
        
        print(nums)
        while(h<len(nums)):
            if nums[h]==replace:
                g = h+1
                while(g<len(nums) and (nums[g]==replace)):
                    g+=1
                if g<len(nums):
                    nums[h],nums[g] = nums[g],nums[h]
            h+=1
        print(kk)
        return kk


        