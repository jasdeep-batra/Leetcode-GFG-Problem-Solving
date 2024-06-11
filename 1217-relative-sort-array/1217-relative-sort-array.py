class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        for i in arr2:
            j = freq[i]
            for k in range(j):
                res.append(i)
            freq[i] = -1
        rem = []
        for i in arr1:
            if freq[i]!=-1:
                rem.append(i)
        rem.sort()
        res+=rem
        return res
        