// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    //Function to find the next greater element for each element of the array.
    vector<long long> nextLargerElement(vector<long long> arr, int n){
        stack<long long> s;
        vector<long long> result;
        for(int i=n-1;i>=0;i--)
        {
            long long ans = -1;
            while(!(s.empty()))
            {
                if(s.top()<arr[i])
                {
                    s.pop();
                }
                else
                {
                    break;
                }
            }
            if(!(s.empty())) ans = s.top();
            else ans = -1;
            s.push(arr[i]);
            result.push_back(ans);
        }
        reverse(result.begin(),result.end());
        return result;
    }
};

// { Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        
        int n;
        cin>>n;
        vector<long long> arr(n);
        for(int i=0;i<n;i++)
            cin>>arr[i];
        
        Solution obj;
        vector <long long> res = obj.nextLargerElement(arr, n);
        for (long long i : res) cout << i << " ";
        cout<<endl;
    }
	return 0;
}  // } Driver Code Ends