class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        odd_count = 1
        even_count = 0
        ans = 0
        if arr[0]%2==0:
            odd_count = 0
            even_count = 1
        
        for i in range(1,len(arr)):
            ans+=(odd_count)
            if arr[i]%2==0:         
                even_count = 1+even_count       
            else:
                temp = odd_count
                odd_count = 1+even_count
                even_count = temp
        ans+=odd_count
        return ans%MOD



        