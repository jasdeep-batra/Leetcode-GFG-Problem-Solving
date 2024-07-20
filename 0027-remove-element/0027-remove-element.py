class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i=0
        while i<len(nums):
            if nums[i] == val:
                nums[i] = 101
                nums.pop(i)
                nums.append(101)
                k+=1
                continue
            i+=1
        return len(nums)-k
