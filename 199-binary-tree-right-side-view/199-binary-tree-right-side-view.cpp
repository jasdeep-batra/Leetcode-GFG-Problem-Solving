/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* root, map<int,int> &mp,int level)
    {
        if(root==NULL)return;
        mp[level] = root->val;
        dfs(root->left,mp,level+1);
        dfs(root->right,mp,level+1);
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        map<int,int> mp;
        dfs(root,mp,0);
        for(auto itr: mp)
        {
            result.push_back(itr.second);
        }
        return result;
    }
};