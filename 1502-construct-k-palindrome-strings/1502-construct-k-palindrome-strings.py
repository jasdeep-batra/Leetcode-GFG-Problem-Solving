class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #we have to partition the string
        mapp = Counter(s)
        #if we have odd characters then always we will have > k palindromes
        #why because you can't use the
        if len(s) < k:
            return False
        count = 0
        for key,value in mapp.items():
            if value%2!=0:
                count+=1

        if count>k:
            return False
        return True

        