// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int i =1;
        int j = n;
        int ans = 0;
        while(i<=j)
        {
            int mid = i+(j-i)/2;
            cout<<"mid"<<mid<<endl;
            bool res = isBadVersion(mid);
            if(res==false)
            {
                ans = mid;
                i = mid+1;
                cout<<"i"<<i<<endl;
            }
            else if(res==true){
                j = mid-1;
                cout<<"j"<<j<<endl;
            }            
        }
        return ans+1;
    }
};