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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(root==NULL)return result;
        map<int,vector<int>> mp;
        queue<pair<TreeNode*, int>> q;
        q.push({root,0});
        while(!(q.empty()))
        {
            TreeNode* n = q.front().first;
            int level = q.front().second;
            mp[level].push_back(n->val);
            q.pop();
            if(n->left)
            {
                q.push({n->left,level+1});
            }
            if(n->right)
            {
                q.push({n->right,level+1});
            }
        }
        for(auto itr:mp)
        {
            result.push_back(itr.second);
        }
        return result;
    }
};