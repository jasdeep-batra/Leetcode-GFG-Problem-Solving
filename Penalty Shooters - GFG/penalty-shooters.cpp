// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function Template for C++

class Solution{
public:
    vector<int> goals(int X, int Y, int Z){
        int geek = 0;
        int nerd = 0;
        while(Z!=1)
        {
            if(((X >= Z && X%Z==0) && (Y >= Z && Y%Z==0)) || (X >= Z && X%Z==0))
            {
                geek++;
                X--;
            }
            else if(Y >= Z && Y%Z==0)
            {
                nerd++;
                Y--;
            }
            else
            {
                Z--;
            }
        }
        vector<int> res = {geek,nerd};
        return res;
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int X, Y, Z;
        cin>>X>>Y>>Z;
        
        Solution ob;
        vector<int> ans = ob.goals(X, Y, Z);
        cout<<ans[0]<<" "<<ans[1]<<"\n";
    }
    return 0;
}  // } Driver Code Ends