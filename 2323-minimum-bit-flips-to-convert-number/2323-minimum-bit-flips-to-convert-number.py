class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_aa = bin(start)
        bin_bb = bin(goal)
        bin_a = bin_aa[2:]
        bin_b = bin_bb[2:]
        # print(bin_a,bin_b)
        # xor operator means if 1 xor 1 = 0
        # 0 xor 0 = 0
        # 1 xor 0  = 1
        # 0 xor 1 = 1
        if len(bin_b) > len(bin_a):
            bin_a,bin_b = bin_b,bin_a
        if len(bin_a) > len(bin_b):
            add  = "0"*1
            bin_b = "0"*(len(bin_a)-len(bin_b)) + bin_b#
            # print(bin_b)
        ans = 0
        # print(bin_a,bin_b)
        for i in range(len(bin_a)):
            if bin_b[i]!=bin_a[i]:
                ans+=1

        return ans


        