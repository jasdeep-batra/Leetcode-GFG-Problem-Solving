// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


class Solution
{
    public:
    //Function to calculate the span of stockâ€™s price for all n days.
    vector <int> calculateSpan(int price[], int n)
    {
        vector<int> result;
        stack<pair<int,int>> s;
        for(int i=0;i<n;i++)
        {
           int ans = -1;
           while(!(s.empty()))
           {
               if(s.top().first <= price[i])
               {
                   s.pop();
               }
               else
               {
                   break;
               }
           }
           if(!(s.empty())) ans = s.top().second;
            else ans = -1;
           s.push(make_pair(price[i],i));
           result.push_back(ans);
        }
        for(int i=0;i<n;i++)
        {
            result[i] = i - result[i];
        }
        return result;
    }
};



// { Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int i,a[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
		}
		Solution obj;
		vector <int> s = obj.calculateSpan(a, n);
		
		for(i=0;i<n;i++)
		{
			cout<<s[i]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
  // } Driver Code Ends