class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            a = len(str1)
            prefix = str2[0:a]
            suffix = str2[len(str2)-a:]
            if (prefix==str1) and (suffix==str1):
                return True
            return False
        # words.sort()
        ans = 0
        for j in range(len(words)-1,-1,-1):
            for i in range(0,j):
                if len(words[j]) < len(words[i]):
                    continue
                ans+=isPrefixAndSuffix(words[i],words[j])

        return ans


        