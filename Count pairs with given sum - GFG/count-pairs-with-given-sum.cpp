// { Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{   
public:
    int getPairsCount(int arr[], int n, int k) {
        // code here
        int res = 0;
        map<int,int> mp;
        //mp[0] = 1;
        vector<int> nums(100000,0);
        for(int i=0;i<n;i++)
        {
            //nums[arr[i]] = 1;
            mp[arr[i]]++;
        }
        for(int i=0;i<n;i++)
        {
            //if(i.first>k)continue;
            mp[arr[i]]--;
            if(mp.find(k-arr[i])!=mp.end()){
                //cout<<i.first<<" "<<k-i.first<<endl;
                res+=mp[k-arr[i]];
                //nums[i.first]--;
            }
            //nums[arr[i]] = 1;
        }
        //cout<<res;
        return res;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.getPairsCount(arr, n, k);
        cout << ans << "\n";
    }
    
    return 0;
}  // } Driver Code Ends