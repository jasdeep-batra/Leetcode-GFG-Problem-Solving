// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    vector<vector<int> > subsets(vector<int>& A)
    {
        vector<vector<int> >result; 
        int size = pow(2,A.size());
        for(int i=0;i<size;i++)
        {
            vector<int> temp;
            int curr = i;
            int cnt = 0;
            while(curr)
            {
                if(curr&1)
                {
                    temp.push_back(A[cnt]);
                }
                cnt++;
                curr = curr>>1;
            }
            result.push_back(temp);
        }
        sort(result.begin(),result.end());
        return result;
    }
};

// { Driver Code Starts.

int main()
{
	int t;
	cin >> t;

	while (t--)
	{
		int n, x;
		cin >> n;

		vector<int> array;
		for (int i = 0; i < n; i++)
		{
			cin >> x;
			array.push_back(x);
		}
        
        
        Solution ob;
		vector<vector<int> > res = ob.subsets(array);

		// Print result
		for (int i = 0; i < res.size(); i++) {
			for (int j = 0; j < res[i].size(); j++)
				cout << res[i][j] << " ";
			cout << endl;
		}

		
	}

	return 0;
}  // } Driver Code Ends