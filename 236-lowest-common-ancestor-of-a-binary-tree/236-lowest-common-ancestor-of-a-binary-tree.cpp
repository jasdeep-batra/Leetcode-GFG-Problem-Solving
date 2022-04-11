/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void traverse(TreeNode* root, map<TreeNode*, pair<TreeNode*,int>>& mp)
    {
        if(root==NULL)return;
        queue<pair<TreeNode*,int>> q;
        q.push({root,0});
        mp[root] = {root,0};
        while(!q.empty())
        {
            int lev = q.front().second;
            TreeNode* nod = q.front().first;
            q.pop();
            if(nod->left)
            {
                mp[nod->left] = {nod,lev+1};
                q.push({nod->left,lev+1});
            }
            if(nod->right)
            {
                mp[nod->right] = {nod,lev+1};
                q.push({nod->right,lev+1});
            }
        }
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        map<TreeNode*, pair<TreeNode*,int>> mp; // parent,level
        for(auto itr: mp)
        {
            cout<<itr.first<<endl;
        }
        traverse(root,mp);
        TreeNode* top = p;
        TreeNode* down = q;
        if(mp[top].second > mp[down].second){
            top = q;
            down = p;
        }
        while(top!=root)
        {
            int level1 = mp[top].second;
            int level2 = mp[down].second;
            TreeNode* parent1 = mp[down].first;
            if(parent1==top){
                return top;
            } 
            if(parent1==mp[top].first)
            {
                return mp[top].first; 
            }     
            if(level1==level2)
            {
                top = mp[top].first;
                down = mp[down].first;
            }
            else
            {
                down = mp[down].first;
            }
        }
        return root;
    }
};