class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        i,j = min(bloomDay),max(bloomDay)
        ans = j
        def count_bq(days):
            consicutive = 0
            window = 0
            for day in bloomDay:
                if day <= days:
                    consicutive+=1
                    if consicutive==k:
                        window+=1
                        consicutive = 0
                else:
                    consicutive = 0

            return window
        while j>i:
            mid = (j+i)//2
            # mid == days
            countBk = count_bq(mid)
            if countBk >= m:
                ans = min(ans,mid)
                j = mid
            else:
                i = mid+1

        return ans