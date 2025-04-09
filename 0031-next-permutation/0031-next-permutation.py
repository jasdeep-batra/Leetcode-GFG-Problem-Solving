class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # def recursion(i):
        #     if i==n-1:
        #         if nums[i] > nums[i-1]
        #         return nums[i]
        #     return nums[i-1]

        #     if recursion(i+1)==True:
        flag = -1
        def swap(a,b):
            a,b = b,a
            return 
        # find buldge (because there the next permutation will form)
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                flag = i-1
                break
        if flag==-1:
            return nums.reverse()
        
        #find minimum element and its index
        min_ele = sys.maxsize
        min_ind = len(nums)-1
        for i in range(len(nums)-1,flag,-1):
            if nums[i] > nums[flag]:
                if min_ele > nums[i]:
                    min_ele = nums[i]
                    min_ind = i

        nums[flag],nums[min_ind] = nums[min_ind],nums[flag]
        nums[flag+1:] = sorted(nums[flag+1:])
            
        







        """
        Do not return anything, modify nums in-place instead.
        """
        