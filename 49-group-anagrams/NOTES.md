class Solution {
public:
vector<vector<string>> groupAnagrams(vector<string>& strs) {
vector<vector<string>> result;
map<string,vector<int>> mp;
for(int i=0;i<strs.size();i++)
{
string temp = strs[i];
sort(temp.begin(),temp.end());
mp[temp].push_back(i);
}
for(auto itr: mp)
{
vector<int> temp;vector<string> anagam;
temp = itr.second;
for(int i=0;i<temp.size();i++)
{
anagram.push_back(strs[temp[i]]);
}
result.push_back(anagram);
}
}
};