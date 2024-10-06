class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Ensure sentence1 is the longer sentence
        if len(sentence1.split()) < len(sentence2.split()):
            sentence1, sentence2 = sentence2, sentence1

        # Split both sentences into word lists
        s1 = sentence1.split()
        s2 = sentence2.split()

        # Now, let's check if sentence2 can be a prefix or suffix of sentence1
        i, j = 0, 0
        # Check prefix similarity
        while i < len(s2) and s1[i] == s2[i]:
            i += 1
        
        # Check suffix similarity
        while j < len(s2) and s1[-(j + 1)] == s2[-(j + 1)]:
            j += 1

        # They are similar if the total matched (prefix + suffix) is at least the length of s2
        return i + j >= len(s2)
