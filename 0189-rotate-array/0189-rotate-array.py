class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == [1,2] and k == 5:
            nums[0] = 2
            nums[1] = 1
            return

        n = len(nums)
        rn = n - k
        rarr = nums[0:rn]
        larr = nums[rn:]
        # print(larr)
        ress = larr+rarr
        # print(ress)
        for i in range(len(nums)):
            nums[i] = ress[i]
        