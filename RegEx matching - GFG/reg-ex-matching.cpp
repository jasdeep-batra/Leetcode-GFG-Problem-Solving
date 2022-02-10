// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    int isPatternPresent(string S, string P) {
        char start = P[0];
        char end = P[P.size()-1];
        if(start=='^')
        {
            int i = 1;
            while(i<P.size())
            {
                if(P[i]!=S[i-1])
                {
                    return 0;
                }
                i++;
            }
            if(i==P.size())return 1;
        }
        if(end=='$')
        {
            int i = P.size()-2,j=S.size()-1;
            while(i>=0)
            {
                if(P[i]!=S[j])
                {
                    return 0;
                }
                i--;j--;
            }
            if(i==-1)return 1;
        }
        else
        {
            return S.find(P)!=-1;
        }
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string P,S;

        cin>>P;
        cin>>S;

        Solution ob;
        cout << ob.isPatternPresent(S,P) << endl;
    }
    return 0;
}  // } Driver Code Ends