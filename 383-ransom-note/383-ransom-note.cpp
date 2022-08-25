class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        sort(ransomNote.begin(),ransomNote.end());
        sort(magazine.begin(),magazine.end());
        int i=0;int j=0;
        while(i<magazine.size())
        {
            if(ransomNote[j]==magazine[i])
            {
                j++;
            }
            if(j==ransomNote.size())return true;
            i++;
        }
        return false;
    }
};