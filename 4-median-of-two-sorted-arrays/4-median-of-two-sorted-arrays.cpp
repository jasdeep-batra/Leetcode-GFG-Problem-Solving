class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        if(n1>n2) return findMedianSortedArrays(nums2,nums1);
        
        double median= 0.00;
        int size = (n1+n2+1)/2;
        int first = 0;
        int last = n1;
        while(last>=first)
        {
            int mid = (last+first)/2;
            int part = size - mid;
            int l1 = (mid==0) ? INT_MIN : nums1[mid-1];
            int r1 = (mid==n1) ? INT_MAX : nums1[mid];
            
            int l2 = (part==0) ? INT_MIN : nums2[part-1];
            int r2 = (part==n2) ? INT_MAX : nums2[part];
            
            if(l1 <= r2 && r1 >= l2)
            {
                if((n1+n2)%2==0)
                {
                    return (max(l1,l2) + min(r1, r2))/2.0;
                }
                else
                {
                    return max(l1,l2);
                }
            }
            if(r1 < l2)
            {
                first = mid+1;
            }
            else if(l1 > r2)
            {
                last = mid-1;
            }
        }
        return median;
        
    }
};