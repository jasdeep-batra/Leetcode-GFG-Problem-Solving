class Solution:
    def get_freq(self, word):
        frequency = [0] * 26
        for char in word:
            frequency[ord(char) - ord('a')] += 1
        return frequency

    def common(self, freq1, freq2):
        return [min(f1, f2) for f1, f2 in zip(freq1, freq2)]
    def commonChars(self, words: List[str]) -> List[str]:
        latest_frequency = self.get_freq(words[0])
        for word in words[1:]:
            latest_frequency = self.common(latest_frequency,self.get_freq(word))

        result = []
        for i in range(26):
            result.extend([chr(i+ord('a'))]*latest_frequency[i]) 
        
        return result;