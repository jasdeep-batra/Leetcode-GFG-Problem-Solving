class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        summ = sum(chalk)
        iterations = summ//k
        remainder = k%summ
        # print(remainder)
        for i in range(len(chalk)):
            if remainder >= chalk[i]:
                remainder-=chalk[i]
            else:
                return i
        return remainder
            


        