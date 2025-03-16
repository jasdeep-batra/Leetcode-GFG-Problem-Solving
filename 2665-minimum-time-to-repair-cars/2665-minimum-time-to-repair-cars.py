class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #can we determine maximum time 
        r = max(ranks)
        left,right = 1, (r*cars*cars)
        # 400 min
        ranks.sort()

        def helper(mid):
            count = 0
            for item in ranks:
                count += int(math.sqrt(mid//item))
            return True if count>=cars else False


        ans = right
        while right >= left:
            mid = (right+left)//2
            if  helper(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans


