class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        arr = []
        window = len(cardPoints)-k

        i=0
        ans = 0
        res = float('inf')
        for j in range(0,len(cardPoints)):
            ans+=cardPoints[j]
            if (j-i+1) > window:
                ans-=cardPoints[i]
                i+=1
            if (j-i+1)==window:
                res = min(ans,res)
        # print(res)
        return sum(cardPoints)-res
