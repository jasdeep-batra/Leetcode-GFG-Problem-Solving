class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #local problem and k times you can change
        #get more freq one for each window
        count = {}
        i = 0
        ans = 0
        max_freq = 0
        for j in range(len(answerKey)):
            count[answerKey[j]] = count.get(answerKey[j],0)+1
            max_freq = max(max_freq,count[answerKey[j]])

            while (j-i+1) - max_freq > k:
                count[answerKey[i]]-=1
                i+=1

            ans = max(ans,(j-i+1))


        return ans

            
