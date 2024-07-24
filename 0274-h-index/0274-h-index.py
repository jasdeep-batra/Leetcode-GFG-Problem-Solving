class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def count(cit:List[int],val):
            cnt = 0
            for i in cit:
                if i>=val:
                    cnt+=1
            return cnt

        j = len(citations)
        i = 1
        ans = 0
        while i<=j:
            mid = (i+j)//2
            curr_count = count(citations,mid)
            if curr_count >= mid:
                ans = max(ans,mid)
                i = mid+1
            else:
                j = mid-1
        return ans
        