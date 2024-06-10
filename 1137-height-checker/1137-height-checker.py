class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sh = list(heights)
        sh.sort()

        cnt = 0
        for i,j in zip(sh,heights):
            # print(i,j)
            if i!=j:
                cnt+=1
        return cnt

        