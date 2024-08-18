class Solution {
public:
    int nthUglyNumber(int n) {
        int a = 2;
        int b = 3;
        int c = 5;
        int k = 1,l=1,m=1;
        vector<int> res;
        res.push_back(1);
        for(int i=1;i<n;i++)
        {
            int small = min(a,min(b,c));
            res.push_back(small);
            if(small==a)
            {
                a = res[k]*2;
                k++;
            }
            if(small==b)
            {
                b = res[l++]*3;
            }
            if(small==c)
            {
                c = res[m++]*5;
            }
        }
        return res[n-1];
    }
};