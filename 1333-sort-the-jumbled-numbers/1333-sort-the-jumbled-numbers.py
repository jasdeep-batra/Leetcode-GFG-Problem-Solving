class Solution:
    def equivalent(self,num,mappings):
        ans = ""
        for i in num:
            j = int(i)
            c = mappings[j]
            cc = str(c)
            ans+=cc
        return ans


    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        ans = {}
        for item in nums:
            sitem = str(item)
            equi = self.equivalent(sitem,mapping)
            equin = int(equi)
            ans[item] = equin

        nums.sort(key = lambda val:ans[val])
        return nums
        
        