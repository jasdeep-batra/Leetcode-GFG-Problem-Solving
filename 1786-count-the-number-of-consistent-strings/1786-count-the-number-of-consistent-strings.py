class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        #brute force
        count = 0
        for item in words:
            for i in item:
                if i not in allowed:
                    count+=1
                    break

        return len(words)-count

        