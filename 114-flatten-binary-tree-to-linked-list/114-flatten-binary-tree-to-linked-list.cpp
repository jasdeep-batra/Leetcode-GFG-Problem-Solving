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
    void preorder(TreeNode* root, queue<TreeNode*>& qt)
    {
        if(root==NULL)
        {
            return;
        }
        qt.push(root);
        preorder(root->left,qt);
        preorder(root->right,qt);
    }
    void flatten(TreeNode* root) {
        if(root==nullptr)return;
        queue<TreeNode*> qt;
        preorder(root,qt);
        qt.pop();
        TreeNode* temp = root;
        while(!qt.empty())
        {
            //cout<<qt.front()->val<<" ";
            temp->left=NULL;temp->right=NULL;
            temp->right = qt.front(); 
            temp = temp->right;
            
            qt.pop();
            
        }
    }
};