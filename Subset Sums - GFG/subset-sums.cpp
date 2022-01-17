// { Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
class Solution
{
public:
    vector<int> result;
    
    void subsetSums(vector<int> arr, int n,int sum)
    {
        if(n==0)
        {
            result.push_back(sum);
            return;
        }
        subsetSums(arr,n-1,arr[n-1]+sum);
        subsetSums(arr,n-1,sum);
    }
    vector<int> subsetSums(vector<int> arr, int N)
    {
        subsetSums(arr,N,0);
        sort(result.begin(),result.end());
        return result;
        
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}  // } Driver Code Ends