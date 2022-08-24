class Solution {
public:
    
    int findMinDifference(vector<string>& timePoints) {
        //basic string problem
        // 00.00 to 11:60
        // 9:56 , 10:45
        // 10.00 9.56
        vector<int> minutes;
        for(int i=0;i<timePoints.size();i++)
        {
            string hr = timePoints[i].substr(0,2);
            string mnt = timePoints[i].substr(3,2);
            int hrr = stoi(hr);
            int mntt = stoi(mnt);
            int time_in_minutes = (hrr*60)+mntt;
            //cout<<time_in_minutes<<endl;
            minutes.push_back(time_in_minutes);
            // 9:56 10:00 - 9:60  10:15
        }
        sort(minutes.begin(),minutes.end());
        int ans = INT_MAX;
        for(int i=1;i<minutes.size();i++)
        {
            //cout<<minutes[i-1]<<" "<<minutes[i]<<endl;
            ans = min(ans,(minutes[i]-minutes[i-1]));
        }
        ans = min(ans,minutes[0]-minutes[minutes.size()-1]+24*60);
        return ans;
    }
};