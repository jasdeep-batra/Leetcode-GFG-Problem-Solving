class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = []*26
        res = ""
        for i in s:
            num_for_i = ord(i)-ord('a')+1
            res+=str(num_for_i)

        resi = int(res)
        def sumitt(ss):
            return sum(int(item) for item in str(ss))
        for _ in range(k):
            resi = sumitt(resi)
        
        

        return resi


            
        