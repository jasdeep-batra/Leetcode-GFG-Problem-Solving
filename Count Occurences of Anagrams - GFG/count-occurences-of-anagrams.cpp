// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


 // } Driver Code Ends
//User function template for C++
class Solution{
public:
	int search(string pat, string txt) {
	    int i = 0;
	    int j = 0;
	    int k = pat.size();
	    int size = txt.size();
	    map<char,int> mp;
	    for(int g=0;g<k;g++)
	    {
	        mp[pat[g]]++;
	    }
	    int count = mp.size(),ans = 0;
	    //string ana;
	    while(j<size)
	    {
	        //cout<<"test: "<<txt[j]<<endl;
	        if(mp.find(txt[j])!=mp.end())
	        {
	            mp[txt[j]]--;
	            //cout<<"map: "<<txt[j]<<" : "<<mp[txt[j]]<<endl;
                if(mp[txt[j]]==0){
                     count--;
                }
	       
	        }
	         //cout<<"count: "<<count<<endl;
	        if(j-i+1 < k)
	        {
	            j++;
	        }
	        else
	        {
	            if(count==0){
	                //cout<<"working"<<endl;
	                ans++;
	            }
	            if(mp.find(txt[i])!=mp.end())
	            {
	                mp[txt[i]]++;
	                if(mp[txt[i]]==1)count++;
	           
	                
	       
	            }
	            //cout<<"ncount: "<<count<<endl;
    	        i++;
    	        j++;
	        }
	    }
	    return ans;
	}

};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string pat, txt;
        cin >> txt >> pat;
        Solution ob;
        auto ans = ob.search(pat, txt);
        cout << ans << "\n";
    }
    return 0;
}  // } Driver Code Ends