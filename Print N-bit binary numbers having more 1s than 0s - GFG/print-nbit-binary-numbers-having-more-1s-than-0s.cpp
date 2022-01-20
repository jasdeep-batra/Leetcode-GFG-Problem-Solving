// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function template for C++
class Solution{
public:	
    vector<string> result;
    void recur(int n,int one, int zero, string res)
    {
        if(n==0)
        {
            result.push_back(res);
            return;
        }
        if(one==zero)
        {
            recur(n-1,one+1,zero,res+'1');
        }
        else
        {
            recur(n-1,one+1,zero,res+'1');
            recur(n-1,one,zero+1,res+'0');
        }
    }
	vector<string> NBitBinary(int N)
	{
	    string res;
	    recur(N,0,0,res);
	    return result;
	}
};

// { Driver Code Starts.

int main() 
{
   	

   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		int n;
   		cin >> n;
        Solution ob;
   		vector<string> ans = ob.NBitBinary(n);

   		for(auto i:ans)
   			cout << i << " ";

   		cout << "\n";
   	}

    return 0;
}  // } Driver Code Ends