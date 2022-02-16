// { Driver Code Starts
// Initial Template for c++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public: 
    vector<vector<int>> dp;
    bool ispalindrome(string str,int i,int j)
    {
        int a=i,b=j;
        while(a<b)
        {
            if(str[a]!=str[b])
            {
                return false;
            }
            a++;
            b--;
        }
        return true;
    }
    int partition(string str, int i, int j)
    {
        if(i>=j)
        {
            return 0;
        }
        int ans = INT_MAX;
        if(ispalindrome(str,i,j))
        {
            return 0;
        }
        if(dp[i][j]!=-1)
        {
            return dp[i][j];
        }
        for(int k=i;k<j;k++)//j = n-1
        {
            int right, left;
            if(dp[i][k]!=-1)
            {
                left = dp[i][k];
            }
            else
            {
                left = partition(str,i,k);
            }
            if(dp[k+1][j]!=-1)
            {
                right = dp[k+1][j];
            }
            else
            {
                right = partition(str,k+1,j);
            }
            int temp = 1 + left + right;
            if(temp<ans)
            {
                ans = temp;
            }
        }
        return dp[i][j] = ans;
    }
    int palindromicPartition(string str)
    {
        dp.resize(1001,vector<int>(1001,-1));
        return partition(str,0,str.size()-1);
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        string str;
        cin>>str;
        
        Solution ob;
        cout<<ob.palindromicPartition(str)<<"\n";
    }
    return 0;
}  // } Driver Code Ends