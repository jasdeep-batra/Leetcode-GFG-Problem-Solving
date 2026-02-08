class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #try previous logic
        def helper(n):
            odd = 0
            i = 0
            ans = 0
            for j in range(len(nums)):
                if nums[j]%2==1:
                    odd+=1

                while odd > n:
                    if nums[i]%2==1:
                        odd-=1
                    i+=1
                

                ans+=(j-i+1)

            return ans

        return helper(k)-helper(k-1)

