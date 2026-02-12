class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = Counter(words)
        gap = len(words[0])
        window = len(words)
        res = []
        for off in range(gap):
            i = off
            local_count = defaultdict(int)
            cnt = 0
            for j in range(i,len(s)-gap+1,gap):
                word = s[j:j+gap]
                if word in count:
                    local_count[word]+=1
                    cnt+=1 # why are u confused here it should get incremetnal everytime word is found as we are handling freq here not just length of map 
                
                    #shrink the window
                    while local_count[word] > count[word]:
                        rem_word = s[i:i+gap]
                        local_count[rem_word]-=1
                        cnt-=1
                        i+=gap

                    if cnt==window:
                        res.append(i)
                else:
                    i = j+gap
                    local_count.clear()
                    cnt = 0

        return res
                    



