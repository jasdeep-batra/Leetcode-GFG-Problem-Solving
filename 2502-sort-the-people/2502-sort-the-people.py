class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res_d = [[height,name] for height,name in zip(heights,names)]
        res_d.sort(reverse=True)

        res = [item[1] for item in res_d]
        return res
        