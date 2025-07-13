class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = defaultdict(int)
        dictt[0] = 1
        summ = 0
        ans = 0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ-k in dictt:
                ans+=dictt[summ-k]
            dictt[summ]+=1
        return ans