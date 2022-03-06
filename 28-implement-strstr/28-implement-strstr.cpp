class Solution {
public:
    int strStr(string haystack, string needle) {
        if(haystack.size()<needle.size())return -1;
        int len = needle.size();
        for(int i=0;i<=haystack.size()-len;i++)
        {
            string check = haystack.substr(i,len);
            if(check==needle)return i;
        }
        return -1;
    }
};