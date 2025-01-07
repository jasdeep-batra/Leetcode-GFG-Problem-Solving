class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if words[i] in words[j]:
                        if words[i] not in res:
                            res.append(words[i])

        return res

            
        