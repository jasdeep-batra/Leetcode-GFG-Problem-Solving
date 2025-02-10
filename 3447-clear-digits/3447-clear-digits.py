class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        sarr = list(s)
        for index,char in enumerate(sarr):
            if char.isalpha():
                stack.append(index)
            else:
                if len(stack)>0:
                    popi = stack.pop()
                sarr[popi] = '@'
                sarr[index] = '@'

        print(sarr)
        nsarr = [char for char in sarr if char!='@']
        return "".join(nsarr)

                
            
        