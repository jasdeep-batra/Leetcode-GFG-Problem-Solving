class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] & 1:
                count+=1
            else:
                count = 0
            if count==3:
                return True

        return False if count!=3 else True