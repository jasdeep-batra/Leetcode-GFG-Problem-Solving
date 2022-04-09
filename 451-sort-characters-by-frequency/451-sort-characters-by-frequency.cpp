class Solution {
public:
    string frequencySort(string s) {
        //naive appraoach
        //with worst space complexity
        sort(s.begin(),s.end());
        int i=0,j=0;
        priority_queue<pair<int,char>> pq;
        while(j<s.size())
        {
            if(s[i]==s[j])j++;
            else
            {
                pq.push({j-i,s[i]});
                i = j;
            }
        }
        pq.push({j-i,s[i]});
        string res;
        while(pq.empty()==false)
        {
            int k = pq.top().first;
            while(k>0)
            {
                res+=pq.top().second;
                k--;
            }
            pq.pop();
        }
        return res;
    }
};