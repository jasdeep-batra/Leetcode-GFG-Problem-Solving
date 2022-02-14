// { Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    int dp[1001][1001];
    int MCM(int arr[], int i, int j)// j = n-1 , i = 1;
    {
        if(i>=j)
        {
            return 0;
        }
        if(dp[i][j]!=-1)
        {
            return dp[i][j];
        }
        int minans = INT_MAX;
        for(int k = i;k<j;k++)
        {
            int ans = MCM(arr,i,k) + MCM(arr,k+1,j) + (arr[i-1]*arr[k]*arr[j]);
            if(ans<minans)
            {
                minans = ans;
            }
        }
        return dp[i][j] = minans;
    }
    int matrixMultiplication(int N, int arr[])
    {
       
        memset(dp,-1,sizeof(dp));
        int answer;
        answer = MCM(arr,1,N-1);
        return answer;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[N];
        for(int i = 0;i < N;i++)
            cin>>arr[i];
        
        Solution ob;
        cout<<ob.matrixMultiplication(N, arr)<<endl;
    }
    return 0;
}  // } Driver Code Ends