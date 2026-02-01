class Tweet:
    def __init__(self,val,time):
        self.next = None
        self.prev = None
        self.val = val
        self.time = time

class Twitter:

    def __init__(self):
        self.follower_list = {}
        self.user_tweet = {}
        self.time = 1
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follower_list:
            self.follower_list[userId] = set([userId])
        tweet = Tweet(tweetId,self.time)
        self.time+=1
        if userId not in self.user_tweet:
            self.user_tweet[userId] = [tweet,tweet]
        else:
            prev = self.user_tweet[userId][1]
            tweet.prev = prev
            prev.next = tweet
            self.user_tweet[userId][1] = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follower_list:
            return []
        pq = [] #max_heap
        print(self.follower_list)
        for user in self.follower_list[userId]:
            if user not in self.user_tweet:
                continue
            tweet = self.user_tweet[user][1]
            heapq.heappush(pq,(-tweet.time,tweet.val,tweet))
        res = []
        while len(pq):
            curr = heapq.heappop(pq)
            res.append(curr[2].val)
            if len(res)==10:
                return res
            if curr[2].prev:
                child = curr[2].prev
                heapq.heappush(pq,(-child.time,child.val,child))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_list:
            self.follower_list[followerId] = set([followerId,followeeId])
        else:
            self.follower_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_list[followerId].discard(followeeId)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)