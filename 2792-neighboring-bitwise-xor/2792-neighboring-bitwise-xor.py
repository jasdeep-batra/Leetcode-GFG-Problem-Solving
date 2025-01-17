class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # if 1 value could be 0 1 or 1 0

        helper = [0]*(len(derived)+1)
        for i in range(1,len(derived)+1):
            if derived[i-1]==1 and helper[i-1]==0:
                helper[i] = 1
            if derived[i-1]==1 and helper[i-1]==1:
                helper[i] = 0
            if derived[i-1]==0 and helper[i-1]==0:
                helper[i] = 0
            if derived[i-1]==0 and helper[i-1]==1:
                helper[i] = 1

        # print(helper)
        return helper[-1]==helper[0]
            
            





        