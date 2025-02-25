class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9+7
        dp = [[0,0] for i in range(len(arr))]
        dp[0] = [1,0]  #odd,even
        if arr[0]%2==0:
            dp[0] = [0,1]
        for i in range(1,len(arr)):
            odd_count = dp[i-1][0]
            even_count = dp[i-1][1]
            if arr[i]%2==0:                
                dp[i] = [odd_count,1+even_count]
            else:
                dp[i] = [even_count+1,odd_count]
        print(dp)
        return sum([dp[i][0]%MOD for i in range(len(dp))])%MOD



        