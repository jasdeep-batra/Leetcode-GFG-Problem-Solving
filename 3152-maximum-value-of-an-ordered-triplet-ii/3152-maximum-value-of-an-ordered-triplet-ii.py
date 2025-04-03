class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxDiff = 0
        maxElem = 0
        triplet = 0
        for num in nums:
            triplet = max(triplet,maxDiff*num)
            maxDiff = max(maxDiff,maxElem-num)
            maxElem = max(maxElem,num)
        return triplet
        

        