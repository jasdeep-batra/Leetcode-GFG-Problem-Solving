class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int i = 0,peak = -1;
        if(arr.size() <3)return false;
        while(i<arr.size()-1)
        {
            if(arr[i] < arr[i+1])
            {
                i++;
            }
            else if(arr[i]==arr[i+1])
            {
                return false;
            }
            else break;
        }
        if(i==arr.size()-1 || i==0)return false;
        while(i<arr.size()-1)
        {
            if(arr[i] > arr[i+1])
            {
                i++;
            }
            else if(arr[i]==arr[i+1])
            {
                return false;
            }
            else break;
        }
        if(i==arr.size()-1)return true;
        return false;
    }
};