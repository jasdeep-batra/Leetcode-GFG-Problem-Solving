// { Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends


class Solution
{
	public:
	    vector<string> result;
	    void recursion(string s, int index)
	    {
	        if(index==s.size())
	        {
	            result.push_back(s);
	            return;
	        }
	        if(s[index]=='?')
	        {
	            s[index]='0';
	            recursion(s,index+1);
	            s[index]='1';
	            recursion(s,index+1);
	        }
	        else
	        {
	            recursion(s,index+1);
	        }
	    }
		vector<string> generate_binary_string(string s)
		{
		    recursion(s,0);
		    return result;
		}
};

// { Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
	    string s;
	    cin >> s;
	    Solution ob;
	    vector<string> ans = ob.generate_binary_string(s);
	    for(auto i: ans)
	    	cout << i << " ";
	    cout << "\n";
    }
	return 0;
}  // } Driver Code Ends