class Twitter {
public:
    map<int,vector<pair<int,int>>> mp;
    map<int,vector<int>> Follow;
    int when;
    Twitter() {
        when = 1;
    }
    
    void postTweet(int userId, int tweetId) {
        mp[userId].push_back({when++,tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        vector<pair<int,int>> preresult;
        vector<int> visit(501,0);
        for(auto i:mp[userId])
        {
            if(visit[i.first]==1)continue;
            else{
                preresult.push_back(i);
                visit[i.first] = 1;
            }
        }
        for(auto i: Follow[userId])
        {
            if(i!=0)
            {
                for(auto j:mp[i])
                {
                    if(visit[j.first]==1)continue;
                    else{
                        preresult.push_back(j);
                        visit[j.first] = 1;                        
                    }
                }
            }
        }
        sort(preresult.begin(),preresult.end(),greater<pair<int,int>>());
        vector<int> result;
        if(preresult.size()<10){
            for(auto i:preresult)
            {
                result.push_back(i.second);
            }
        }
        else{
            for(int i=0;i<10;i++)
            {
                result.push_back(preresult[i].second);
            }
        }
        return result;
    }
    
    void follow(int followerId, int followeeId) {
        Follow[followerId].push_back(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        int siz = Follow[followerId].size();
        for(int i=0;i<siz;i++)
        {
            if(Follow[followerId][i]==followeeId){
                Follow[followerId][i] = 0;
            }
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */