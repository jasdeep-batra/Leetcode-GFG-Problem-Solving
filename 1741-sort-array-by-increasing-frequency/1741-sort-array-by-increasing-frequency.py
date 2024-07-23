class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = [0 for _ in range(201)]
        for num in nums:
            count[num+100]+=1
        nums.sort(key=lambda x: (count[x+100],-x))

        return nums
        