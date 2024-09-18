class Solution:
    def largestNumber(self, nums: List[int]) -> str:


        def comparator(x,y):
            if x+y > y+x:
                return -1
            if y+x > x+y:
                return 1
            return 0
        #possibly of stack 
        slist = list(map(str,nums))
        slist.sort(key = cmp_to_key(comparator))
        result = "".join(slist)
    
    # Handle case where the list is all zeros
        return result if result[0] != '0' else '0'
        