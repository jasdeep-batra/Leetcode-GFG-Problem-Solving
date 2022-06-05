// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution
{
public:
    vector<int> singleNumber(vector<int> nums) 
    {
        int xxor = 0;
        vector<int> ans;
        for(auto i:nums)
        {
            xxor = xxor^i;
        }
        //find the last set bit using right shift and & operator
        int cnt = 0, findbit = xxor;
        while(findbit)
        {
            if(findbit & 1)
            {
                break;
            }
            cnt++;
            findbit = findbit>>1;
        }
        int xor1=0 ,xor2 = 0;
        for(int i =0;i<nums.size();i++)
        {
            if(nums[i] & (1<<cnt)) xor1 = xor1^nums[i];
            else xor2 = xor2^nums[i];
        }
        ans = {xor2,xor1};
        sort(ans.begin(),ans.end());
        return ans;
    }
};

// { Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	int n; 
    	cin >> n;
    	vector<int> v(2 * n + 2);
    	for(int i = 0; i < 2 * n + 2; i++)
    		cin >> v[i];
    	Solution ob;
    	vector<int > ans = ob.singleNumber(v);
    	for(auto i: ans)
    		cout << i << " ";
    	cout << "\n";
    }
	return 0;
}  // } Driver Code Ends