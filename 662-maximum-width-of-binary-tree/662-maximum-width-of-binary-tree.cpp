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
    int widthOfBinaryTree(TreeNode* root) {
        queue<pair<TreeNode*,int>> q;
        int ans = 0;
        q.push({root,0});
        while(q.empty()==false)
        {
            int siz = q.size();
            long long min_index = q.front().second;
            int first,last;
            for(int i=0;i<siz;i++)
            {
                long long cur_id = q.front().second - min_index;
                TreeNode* nod = q.front().first;
                q.pop();
                if(i==0) first = cur_id;
                if(i==siz-1)last = cur_id;
                if(nod->left)
                {
                    q.push({nod->left,2*cur_id+1});
                }
                if(nod->right)
                {
                    q.push({nod->right,2*cur_id+2});
                }
            }
            ans = max(ans,last-first+1);
        }
        return ans;
    }
};