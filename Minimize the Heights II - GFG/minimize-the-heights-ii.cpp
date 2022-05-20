// { Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function template for C++
/*
class Solution {
  public:
  int ans;
  int minmax(int arr[],int n)
  {
      vector<int> vt;
      for(int i=0;i<n;i++)
      {
          vt.push_back(arr[i]);
      }
      sort(vt.begin(),vt.end());
      return vt.back()-vt.front();
  }
  void recursion(int arr[], int n, int k, int index,int& finans)
  {
      if(index==n)
      {
          ans = minmax(arr,n);
          finans = min(ans,finans);
          //cout<<ans<<endl;
          return;
      }
      if(arr[index]-k>=0)
      {
        arr[index]-=k;
        recursion(arr,n,k,index+1,finans);
        arr[index]+=k;
      }
      arr[index]+=k;
      recursion(arr,n,k,index+1,finans);
      arr[index]-=k;
  }
    int getMinDiff(int arr[], int n, int k) {
        // minimum possible difference
        int finans = INT_MAX;
        ans = 0;
        recursion(arr,n,k,0,finans);
        return finans;
    }
};
*/
class Solution {
  public:
    int getMinDiff(int arr[], int n, int k) {
        // follow certain observations
        sort(arr,arr+n);
        int ans = arr[n-1]-arr[0];
        int small = arr[0]+k;
        int large = arr[n-1]-k;
        for(int i=1;i<n;i++)
        {
            int mi = min(small,arr[i]-k);
            int ma = max(arr[i-1]+k,large);
            if(mi<0)continue;
            ans = min(ans,ma-mi);
        }
        return ans;
        
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> k;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.getMinDiff(arr, n, k);
        cout << ans << "\n";
    }
    return 0;
}  // } Driver Code Ends