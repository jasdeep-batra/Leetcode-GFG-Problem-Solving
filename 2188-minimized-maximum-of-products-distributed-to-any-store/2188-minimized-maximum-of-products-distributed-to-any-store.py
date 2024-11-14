class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(item_count):
            if item_count==0:
                return False
            store = 0
            for quantity in quantities:
                store += (quantity-1)//(item_count) + 1

                if store > n:
                    return False
            return True

        low = 1
        high = max(quantities)
        ans = -1
        while(high >= low):
            mid = (low+high)//2

            if helper(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

        