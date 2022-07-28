class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        result = {0,1};
        if(n==1)return result;
        int i = 1;
        while(i<n)
        {
            for(int j=result.size()-1;j>=0;j--)
            {
                int x = 1<<i;
                result.push_back(x|result[j]);
            }
            i++;
        }
        // for(auto k: result)
        // {
        //     cout<<k<<endl;
        // }
        return result;
    }
};