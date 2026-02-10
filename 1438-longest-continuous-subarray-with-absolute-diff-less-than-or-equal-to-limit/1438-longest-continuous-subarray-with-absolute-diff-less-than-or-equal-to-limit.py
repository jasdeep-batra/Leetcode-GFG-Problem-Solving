class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mi = deque()
        mx = deque()

        i = 0
        ans= 0
        for j in range(len(nums)):
            while mi and mi[-1] > nums[j]:
                mi.pop()

            mi.append(nums[j])

            while mx and mx[-1] < nums[j]:
                mx.pop()
            
            mx.append(nums[j])

            while i< j and mi and mx and abs(mx[0]-mi[0]) > limit:
                if mx[0]==nums[i]:
                    mx.popleft()
                
                if mi[0]==nums[i]:
                    mi.popleft()

                i+=1

            ans = max(ans,j-i+1)


        return ans
