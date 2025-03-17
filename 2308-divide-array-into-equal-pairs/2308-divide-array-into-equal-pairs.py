class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ans = Counter(nums)
        for key,value in ans.items():
            if value%2!=0:
                return False
        return True
            


        