#include<bits/stdc++.h>
class Solution {
public:
    int max(int x, int y)
    {
        return (x>y)?x:y;
    }
    int leastInterval(vector<char>& tasks, int n) {
        if(n==0)return tasks.size();
        map<char,int> mp;
        for(auto i: tasks)
        {
            mp[i]++;
        }
        priority_queue<pair<int,char>> pm;
        for(auto i:mp)
        {
            pm.push({i.second,i.first});
        }
        int maxx = pm.top().first;
        int ans = (maxx-1)*n+maxx;
        pm.pop();
        while(!pm.empty())
        {
            if(pm.top().first==maxx)
            {
                ans++;
            }
            pm.pop();
        }
        int ansss = max(ans,tasks.size());
        return ansss;
            
    }
};