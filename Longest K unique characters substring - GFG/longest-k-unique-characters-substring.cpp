// { Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{
  public:
    int longestKSubstr(string s, int K) {
        int result  = -1;
        map<char,int> mp;
        int i=0,j=0;
        while(j<s.size())
        {
            mp[s[j]]++;
            if(mp.size()<K)
            {
                
                j++;
            }
            if(mp.size()==K)
            {
                
                result = max(result,j-i+1);
                j++;
            }
            if(mp.size()>K)  // meayl 2
            {
                mp[s[i]]--;
                if(mp[s[i]]==0)
                {
                    mp.erase(s[i]);
                }
                i++;
                j++;
                
            }
        }
        return result;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        Solution ob;
        cout << ob.longestKSubstr(s, k) << endl;
    }
}
  // } Driver Code Ends