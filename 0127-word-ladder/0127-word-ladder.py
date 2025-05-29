class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #how about we create a graph based on single difference in letter
        #but to check the single diff we have to be brute force for now

        #check for if trget is in wordlist
        def checkDiff(word1,word2):
            if len(word1)!=len(word2):
                return False
            else:
                one = False
                for i in range(len(word1)):
                    if word1[i]!=word2[i]:
                        if one:
                            return False
                        one = True                        
            return True

        # create adjacency list
        adj = defaultdict(list)
        for i in range(len(wordList)-1):
            for j in range(i+1,len(wordList)):
                if checkDiff(wordList[i],wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        for item in wordList:
            if checkDiff(item,beginWord):
                adj[beginWord].append(item)
                adj[item].append(beginWord)


        queue = deque()
        visit = set()
        queue.append((beginWord,1))     
        visit.add(beginWord)
        while queue:
            curr,cnt = queue.popleft()
            if curr==endWord:
                return cnt

            for child in adj[curr]:
                if child not in visit:
                    queue.append((child,cnt+1))
                    visit.add(child)

        return 0





        




        