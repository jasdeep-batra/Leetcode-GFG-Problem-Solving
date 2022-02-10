// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
  public:
/*You are required to complete this method*/
    int wildCard(string pattern,string str)
    {
        vector<vector<bool>> dp(pattern.size()+1,vector<bool>(str.size()+1,false));
        dp[0][0] = true;
        for(int i=1;i<pattern.size()+1;i++)
        {
            if(pattern[i-1]=='*')
            {
                dp[i][0] = dp[i-1][0];
            }
        }
        for(int i=1;i<pattern.size()+1;i++)
        {
            for(int j=1;j<str.size()+1;j++)
            {
                if(pattern[i-1]=='*')
                {
                    dp[i][j] = dp[i][j-1] || dp[i-1][j];
                }
                else
                {
                    if(pattern[i-1]==str[j-1] || pattern[i-1]=='?')
                    {
                        dp[i][j] = dp[i-1][j-1];
                    }
                }
            }
        }
        int ans = dp[pattern.size()][str.size()];
        return ans;
        
    }
};

// { Driver Code Starts.
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
           string pat,text;
           cin>>pat;
cin.ignore(numeric_limits<streamsize>::max(),'\n');
           cin>>text;
           Solution obj;
           cout<<obj.wildCard(pat,text)<<endl;
   }
}
  // } Driver Code Ends