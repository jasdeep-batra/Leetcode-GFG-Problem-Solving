class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for item in nums:
            xor^=item

        res = []
        cxor = xor
        for k in range(len(nums)):
            ans = 0
            for i in range(maximumBit):
                if((cxor&(1<<i))==0):
                    ans |= (1<<i)
            res.append(ans)
            cxor = cxor^nums[len(nums)-1-k]
        return res

        #base xor


        