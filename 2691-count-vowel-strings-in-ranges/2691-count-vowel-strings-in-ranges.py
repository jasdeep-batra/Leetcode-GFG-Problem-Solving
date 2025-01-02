class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result =[]
        cache = [0]*(len(words))

        vowel = set(['a','e','i','o','u'])
        ind = 0
        
        for k in range(len(words)):
            if (words[k][0] in vowel) and (words[k][-1] in vowel):
                cache[k]=1
        ncache = []*(len(words)+1)        
        for i in range(1,len(cache)):
            cache[i] = cache[i]+cache[i-1]
            # 1 0 1 1 1 0
            # 1 1 2 3 4 4
        cache = [0] + cache
        print(cache)
        for i,j in queries:
            result.append(cache[j+1]-cache[i])

        return result




        