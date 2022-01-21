class Solution {
public:
    int findMin(vector<int>& nums) {
        int first = 0;
        int last = nums.size()-1;
        int N = nums.size();
        int coun = 12;
        while(last>=first)
        {
            int mid =  (last+first)/2;
            int prev = (mid+N-1)%N;
            int next = (mid+1)%N;
            
            if((nums[mid] < nums[prev]) && (nums[mid] < nums[next]))
            {
                coun = nums[mid];
                return nums[mid];
            }
            else if(nums[mid] < nums[first])
            {
                last = mid-1;
            }
            else if(nums[mid] > nums[last])
            {
                first = mid+1;
            }
            else
            {
                return nums[first];
            }
        }
        cout<<coun<<endl;
        return coun;
    }
};