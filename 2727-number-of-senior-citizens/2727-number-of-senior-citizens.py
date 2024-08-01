class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for st in details:
            # print(st[11:13])
            if int(st[11:13])>60:
                cnt+=1
        return cnt

        