class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #do we need to use 2d array for each array
        #how to compare 
        #KMP Algorithm for finding longeset prefix
        dictt = set()
        ans = 0
        for item in arr1:
            while item>0:
                print(item)
                if(item in dictt):
                    break
                dictt.add(item)
                item = item//10

        for item in arr2:
            while item>0:
                if item in dictt:
                    if item > ans:
                        ans = item
                        break
                item = item//10
        cnt = 0
        while(ans):
            cnt+=1
            ans//=10
        
        return cnt

            



        