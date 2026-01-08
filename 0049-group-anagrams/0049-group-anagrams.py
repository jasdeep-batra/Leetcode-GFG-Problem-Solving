class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key] = [word]

        res = []
        for key,value in anagram.items():
            res.append(value)
        return res