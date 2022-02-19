class Solution {
public:
    vector<int> dp;
    bool canReac(vector<int>& arr, int start)
    {
        if(start<0 || start>arr.size()-1)return false;
        if(arr[start]==0)return true;
        if(dp[start]==-1)
        {
            dp[start] = 1;
            return canReac(arr,start-arr[start]) || canReac(arr,start+arr[start]);
        }
        else
        {
            return false;
        }
    }
    bool canReach(vector<int>& arr, int start) {
      dp.resize(arr.size(),-1);
        return canReac(arr,start);
    }
};