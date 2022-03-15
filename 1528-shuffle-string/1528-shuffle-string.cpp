class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string copy = s;
        for(int i=0;i<indices.size();i++)
        {
            int ind = indices[i];
            char c = s[i];
            copy[ind] = c;
        }
        return copy;
    }
};