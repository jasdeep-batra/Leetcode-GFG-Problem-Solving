// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        // code here
        vector<int> nums(n,1);
        set<int> pr;
        vector<int> result;
        for(int i=0;i<n;i++)
        {
            nums[arr[i]] = -nums[arr[i]];
            if(nums[arr[i]]>0)pr.insert(arr[i]);
        }
        if(pr.empty())result.push_back(-1);
        for(auto i: pr)
        {
            result.push_back(i);
        }
        return result;
    }
};


// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution obj;
        vector<int> ans = obj.duplicates(a, n);
        for (int i : ans) cout << i << ' ';
        cout << endl;
    }
    return 0;
}
  // } Driver Code Ends