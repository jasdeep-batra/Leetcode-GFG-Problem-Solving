class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)  < len(s1):
            return False

        # premutation means any sequence
        #sliding window should solve this

        freq = Counter(s1)

        i = 0

        counter = len(s1)
        for j in range(len(s2)):
            if s2[j] in freq:
                freq[s2[j]]-=1

                if freq[s2[j]]>=0:
                    counter-=1

            while j-i+1 > len(s1):
                if s2[i] in freq:
                    freq[s2[i]]+=1
                    if freq[s2[i]] > 0:
                        counter+=1

                i+=1

            if counter==0:
                return True
        print(counter)
        return False        

