class Solution {
public:
    
    // void binary_rep(int n,int numb){
    //     string ans;
    //     while(n){
    //         int bit = n&1;
    //         ans+=((n&1)+'0');
    //         n>>=1;
    //     }
    //     reverse(ans.begin(),ans.end());
    //     int numb = 0;
    //     for(int i=0;i<ans.size();i++)
    //     {
    //         numb=numb*2+(ans[i]-'0');
    //     }
    //     numb = numb%1000000009;
    // }
    int concatenatedBinary(int n) {
//         int ans = 0;
//         int numb = 0;
//         for(int i=1;i<=n;i++)
//         {
//             binary_rep(i);
//             //cout<<binary_rep(i)<<endl;
//         }
        
//         return numb;
        long ans = 0;
        for(int i=1;i<=n;i++)
        {
            int x = i;
            int len = 0;
            while(x){
                len++;
                x>>=1;
            }
           ans = (ans<<len)%1000000007 + i;
        }
        return ans%1000000007;
    }
};