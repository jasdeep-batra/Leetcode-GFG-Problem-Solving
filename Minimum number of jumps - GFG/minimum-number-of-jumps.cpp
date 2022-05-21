// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution{
  public:
    int minJumps(int arr[], int n){
        if(n==1)return 0;
        if(arr[0]==0)return -1;
        int jump = 0;
        int maxJump = INT_MIN;
        int range = 0;
        for(int i=0;i<n;i++)
        {
            //if(i==n-1)return 0;
            maxJump = max(maxJump,i+arr[i]);
            //from each index what's the max jump you can take;
            if(i==range)
            {
                range = maxJump;
                jump++;
                if(range>=n-1)
                {
                    break;
                }
            }
        }
        if(range>=n-1)
        {
            return jump;
        }
        return -1;
    }
};


// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}
  // } Driver Code Ends