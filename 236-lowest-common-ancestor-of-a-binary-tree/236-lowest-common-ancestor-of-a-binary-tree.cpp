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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==nullptr)
        {
            return nullptr;
        }
        if(root==p || root==q)
        {
            return root;
        }
        TreeNode* n1 = lowestCommonAncestor(root->left,p,q);
        TreeNode* n2 = lowestCommonAncestor(root->right,p,q);
        if(n1==nullptr || n2==nullptr)
        {
            return (n1)?n1:n2;
        }
        if(n1 && n2)
        {
            return root;
        }
        return root;
    }
};