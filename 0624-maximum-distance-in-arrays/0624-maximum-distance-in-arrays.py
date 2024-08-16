class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = arrays[0][0]
        maxi = arrays[0][-1]

        ans = 0
        for i in range(1,len(arrays)):
            arr = arrays[i]
            ans = max(ans,abs(arr[-1]-mini),abs(maxi-arr[0]))
            mini = min(mini,arr[0])
            maxi = max(maxi,arr[-1])

        return ans