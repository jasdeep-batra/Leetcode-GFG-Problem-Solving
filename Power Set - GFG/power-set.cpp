// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
	public:
	    vector<string> result;
	    void rec(string s, string res,int i)
	    {
	        //cout<<"wroking"<<res<<endl;
	        if(i==s.size())
	         {   result.push_back(res);
	            return;}
	        rec(s,res+s[i],i+1);
	        rec(s,res,i+1);
	    }
		vector<string> AllPossibleStrings(string s){
		    string res;
		    rec(s,res,0);
		    
		    result.pop_back();
		    sort(result.begin(),result.end());
		    //cout<<"res[0]: "<<result[0]<<endl;
		    return result;
		}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string s;
		cin >> s;
		Solution ob;
		vector<string> res = ob.AllPossibleStrings(s);
		for(auto i : res)
			cout << i <<" ";
		cout << "\n";

	}
	return 0;
}  // } Driver Code Ends