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
typedef pair<int,int> p;
class Solution {
public:
    //BFS
    map<int,vector<int>> mp;
    void bfs(TreeNode* root,int level)
    {
        if(root==nullptr)return;
        mp[level].push_back(root->val);
        stack<pair<TreeNode*,int>> q;
        stack<pair<TreeNode*,int>> s;
        q.push({root,level});
        int lev = q.top().second;
        while(!q.empty() || !s.empty())
        {
            
            while(!q.empty())
            {
                auto curr = q.top().first;
                lev = q.top().second;
                cout<<"qstack: "<<curr->val<<endl;
                //mp[lev].push_back(curr->val);
                q.pop();
                if(curr->right)
                {
                    mp[lev+1].push_back(curr->right->val);
                    s.push({curr->right,lev+1});                   
                }
                if(curr->left)
                {
                    mp[lev+1].push_back(curr->left->val);           
                    s.push({curr->left,lev+1});                    
                }
            }
            while(!s.empty())
            {
                auto curr = s.top().first;
                lev = s.top().second;
                cout<<"sstack: "<<curr->val<<endl;
                //mp[lev].push_back(curr->val);
                s.pop();
                if(curr->left)
                {
                    mp[lev+1].push_back(curr->left->val);
                    q.push({curr->left,lev+1});
                    
                }
                if(curr->right)
                {
                    mp[lev+1].push_back(curr->right->val);         
                    q.push({curr->right,lev+1});                   
                }
            }
        }        
    }
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        bfs(root,0);
        vector<vector<int>> result;
        for(auto i:mp)
        {
            result.push_back(i.second);
        }
        return result;
        
    }
};