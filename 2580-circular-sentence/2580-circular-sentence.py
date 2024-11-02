class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split()
        if arr[0][0]!= arr[-1][-1]:
            return False
        for i in range(1,len(arr)):
            if arr[i][0]!=arr[i-1][-1]:
                return False
        
        return True

        