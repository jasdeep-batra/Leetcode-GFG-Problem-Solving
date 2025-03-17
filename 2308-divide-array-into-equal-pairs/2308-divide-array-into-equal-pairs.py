class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        xor = 0
        arr = [0]*501
        for item in nums:
            arr[item]+=1
        for item in arr:
            if item%2!=0:
                return False
        return True
            


        