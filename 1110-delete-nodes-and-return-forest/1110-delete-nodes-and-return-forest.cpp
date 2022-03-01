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
    vector<TreeNode*> result;
    TreeNode* find(TreeNode* &root, int value)
    {
        if(root==NULL)return NULL;
        if(root->val==value)
        {
            if(root->left!=NULL) result.push_back(root->left);
            if(root->right!=NULL)result.push_back(root->right);
            root=NULL;
            return NULL;
        }
        root->left = find(root->left,value);
        root->right = find(root->right,value);
        return root;
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
            //vector<TreeNode*> result;
            //result.push_back(root);
            sort(to_delete.begin(),to_delete.end());
            for(int i=to_delete.size()-1;i>=0;i--)
            {
                find(root,to_delete[i]);
            }
            if(root!=NULL) result.push_back(root);
        return result;
    }
};