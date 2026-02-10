class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = deque()
        mi = deque()

        ans = 0
        i = 0
        for j in range(len(nums)):
            while mx and nums[j] > mx[-1]:
                mx.pop()
            
            mx.append(nums[j])

            while mi and nums[j] < mi[-1]:
                mi.pop()

            mi.append(nums[j])

            while i<j and mx and mi and ((mx[0]-mi[0]))*(j-i+1) > k:
                if mx[0] == nums[i]:
                    mx.popleft()
                if mi[0] == nums[i]:
                    mi.popleft()

                i+=1

            ans +=(j-i+1)


        return ans