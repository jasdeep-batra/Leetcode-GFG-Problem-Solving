class KthLargest {
public:
    int k;
    priority_queue<int,vector<int>,greater<int>> pq;
    vector<int> stream;
    KthLargest(int K, vector<int>& nums) {
        k = K;
        int i = 0;
        int r = 0;
        //stream = nums;
        while(i<nums.size())
        {
            if(pq.size()<k)pq.push(nums[i]);
            else
            {
                if(nums[i]>pq.top())
                {
                    pq.pop();
                    pq.push(nums[i]);
                }
            }
            i++;
        }
    }
    
    int add(int val) {
        if(pq.size()<k)pq.push(val);
        else if(val>pq.top()) // ==
        {
            pq.pop();
            pq.push(val);                
        }
        return pq.top();
    }
    
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */