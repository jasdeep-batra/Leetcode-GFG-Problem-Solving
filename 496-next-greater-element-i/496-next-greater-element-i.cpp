class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> mp;
        stack<int> s;
        for(int i=nums2.size()-1;i>=0;i--)
        {
            while( !(s.empty()))
            {
                if( nums2[i] > s.top())
                    s.pop();
                else break;
            }
            if(s.empty())mp[nums2[i]]=-1;
            else mp[nums2[i]] = s.top();
            s.push(nums2[i]);
        }
        vector<int> result;
        for(int i=0;i<nums1.size();i++)
        {
            result.push_back(mp[nums1[i]]);
        }
        return result;
    }
};