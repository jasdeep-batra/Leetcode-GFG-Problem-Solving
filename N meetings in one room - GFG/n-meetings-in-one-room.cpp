// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution
{
    public:
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    int maxMeetings(int start[], int end[], int n)
    {
        vector<pair<int,int>> vt;
        for(int i=0;i<n;i++)
        {
            vt.push_back(make_pair(end[i],start[i]));
        }
        sort(vt.begin(),vt.end());
        int count = 1,i=0,j=1;
        while(j<n)
        {
            if(vt[i].first < vt[j].second)
            {
                i=j;
                j++;
                count++;
            }
            else
            {
                j++;
            }
        }
        return count;
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int start[n], end[n];
        for (int i = 0; i < n; i++) cin >> start[i];

        for (int i = 0; i < n; i++) cin >> end[i];

        Solution ob;
        int ans = ob.maxMeetings(start, end, n);
        cout << ans << endl;
    }
    return 0;
}  // } Driver Code Ends