class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        arr = [0]*7
        value = 0
        for item in tops:
            arr[item]+=1
        for item in bottoms:
            arr[item]+=1
        
        for i in range(1,7):
            if arr[i]>=len(tops):
                value = i
                break
        # print(value)
        if not value:
            return -1
        count1 = tops.count(value)
        count2 = bottoms.count(value)
        if count1 < count2:
            tops,bottoms = bottoms,tops
            count1,count2= count2,count1
        for i in range(len(tops)):
            if tops[i]!=value and bottoms[i]!=value:
                print("true,",tops[i],bottoms[i])
                return -1
        return len(tops)-count1





        