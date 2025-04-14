class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}

        for index,item in enumerate(nums):
            if (target-item) in dictt:
                return [index,dictt[target-item]]
            else:
                dictt[item] = index
        return []

            
        

        