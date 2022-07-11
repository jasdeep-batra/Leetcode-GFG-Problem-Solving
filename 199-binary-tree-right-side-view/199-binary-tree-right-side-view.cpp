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
    vector<int> rightSideView(TreeNode* root) {
        //bfs4
        vector<int> result;
        if(!root)return result;
        queue<pair<TreeNode*,int>> q;
        map<int,stack<int>> mp;
        q.push({root,0});
        while(q.empty()==false)
        {
            auto curr = q.front().first;
            auto lev = q.front().second;
            q.pop();
            mp[lev].push(curr->val);
            if(curr->left)
            {
                q.push({curr->left,lev+1});
            }
            if(curr->right)
            {
                q.push({curr->right,lev+1});
            }
        }
        for(auto i: mp)
        {
            result.push_back(i.second.top());
        }
        return result;
    }
};