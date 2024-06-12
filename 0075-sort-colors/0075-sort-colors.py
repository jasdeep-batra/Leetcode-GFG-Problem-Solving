class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = 0
        white =  0
        blue = 0
        for i in nums:
            if i==0:
                red += 1 
            elif i==1:
                white += 1
            else:
                blue +=1

        i = 0
        while(red>0 or white>0 or blue>0):
            if(red>0):
                nums[i] = 0
                red-=1
            elif white>0:
                nums[i] = 1
                white-=1
            else:
                nums[i] = 2
                blue-=1
            i+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        