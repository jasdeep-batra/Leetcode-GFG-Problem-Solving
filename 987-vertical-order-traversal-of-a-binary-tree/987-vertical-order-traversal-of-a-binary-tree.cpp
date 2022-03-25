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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> result;
        map<int,vector<pair<int,int>>>mp;
        queue<pair<pair<int,int>,TreeNode*>> q;
        q.push({{0,0},root});
        int blevel = 0;
        while(q.empty()==false)
        {
            int blevel = q.front().first.first;
            int lev = q.front().first.second;
            TreeNode* nod = q.front().second;
            q.pop();
            mp[lev].push_back({blevel,nod->val});
            if(nod->left)
            {
                
                q.push({{blevel+1,lev-1},nod->left});
            }
            if(nod->right)
            {
                q.push({{blevel+1,lev+1},nod->right});
            }
        }
        for(auto itr:mp)
        {
            sort(itr.second.begin(),itr.second.end());
            vector<int> temp;
            for(auto it: itr.second)
            {
                temp.push_back(it.second);
            }
            result.push_back(temp);
        }
        return result;
    }
};