class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # if 1 value could be 0 1 or 1 0

        # helper = [0]*(len(derived)+1)

        curr = 0
        for i in range(1,len(derived)+1):
            if derived[i-1]==1:
                if curr==0:
                    curr = 1
                else:
                    curr = 0
            else:
                if curr==0:
                    curr = 0
                else:
                    curr = 1

        # print(helper)
        return curr==0


        
            
            





        