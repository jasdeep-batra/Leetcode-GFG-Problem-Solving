class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        def helper(strn):
            # val = int(strn)
            ans = ""
            # while val:
            #     ans+= str((val & 1) ^ 1)
            #     val >>=1
            # print("ans: ", ans)
            for i in range(len(strn)):
                if strn[i]=='0':
                    ans+='1'
                else:
                    ans+='0'
            return ans[::-1]
        for i in range(n-1):
            invert_s = helper(s)
            
            s = s + "1" + invert_s
            # print("s: ", s)

        return s[k-1]
        