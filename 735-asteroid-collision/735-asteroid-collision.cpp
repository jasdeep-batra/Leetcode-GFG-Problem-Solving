class Solution {
public:
    vector<int> asteroidCollision(vector<int>& arr) {
        vector<int> s;
        int i = 0;
        while(i<arr.size())
        {
            if(s.empty())
            {
                s.push_back(arr[i]);
                i++;
            }
            
            else if(arr[i]<0 && s.back()<0 || arr[i]>0 && s.back()>0)
            {
                cout<<s.back();
                s.push_back(arr[i]);
                i++;
            }
            else if(arr[i]>0 && s.back()<0)
            {
                s.push_back(arr[i]);
                i++;
            }
            else if(arr[i]<0 && s.back()>0)
            {
                if(abs(arr[i])==s.back())
                {
                    s.pop_back();
                    i++;
                }
                else if(abs(arr[i])>=s.back())
                {
                    s.pop_back();
                }
                else
                {
                    i++;
                }
            }
        }
        //reverse(res.begin(),res.end());
        return s;
    }
};