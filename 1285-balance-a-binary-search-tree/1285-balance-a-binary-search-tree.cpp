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
    void inorder_traversal(TreeNode* root, vector<int>& inorder){
        if(root==nullptr){
            return;
        }
        inorder_traversal(root->left,inorder);
        inorder.push_back(root->val);
        inorder_traversal(root->right,inorder);
    }
    TreeNode* buildit(vector<int> inorder, int i, int j)
    {
        if(i>j)return nullptr;
        int mid = i + (j-i)/2;
        TreeNode* nn = new TreeNode(inorder[mid]);
        nn->left = buildit(inorder,i,mid-1);
        nn->right = buildit(inorder,mid+1,j);
        return nn;
        
    }
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> inorder;
        inorder_traversal(root,inorder);
        int n = inorder.size()-1;
        return buildit(inorder,0,n);
    }
    
    
};