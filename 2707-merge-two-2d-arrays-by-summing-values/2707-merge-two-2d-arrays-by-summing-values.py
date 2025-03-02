class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dictt  = {}
        for key,value in nums1:
            if key in dictt:
                dictt[key] += value
            else:
                dictt[key] = value
        for key,value in nums2:
            if key in dictt:
                dictt[key] += value
            else:
                dictt[key] = value
        print(dictt)
        return sorted([[key,value] for key,value in dictt.items()])
        

        


        