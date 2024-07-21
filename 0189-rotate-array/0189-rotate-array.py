class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k%n
        rn = n - k
        rarr = nums[0:rn]
        larr = nums[rn:]
        # print(larr)
        ress = larr+rarr
        # print(ress)
        for i in range(len(nums)):
            nums[i] = ress[i]
        