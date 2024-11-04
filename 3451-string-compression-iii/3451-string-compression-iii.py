class Solution:
    def compressedString(self, word: str) -> str:
        i = 0
        last = word[0]
        ans = ""
        while( i < len(word)):
            k = i+1
            count = 1
            while(k<len(word) and (word[k]==last and count<9)):
                count+=1
                k+=1
            ans+=str(count)+word[i]
            # print(ans)
            i = k
            if i!=len(word):
                last = word[i]

        return ans
        