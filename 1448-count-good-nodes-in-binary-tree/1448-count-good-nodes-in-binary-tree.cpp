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
    int ans = 0;
    void traverse(TreeNode* root, int x){
        if(!root)return;
        if(root->val >= x){
            x = root->val;
            ans++;
        }
        traverse(root->left,x);
        traverse(root->right,x);
    }
    int goodNodes(TreeNode* root) {
        traverse(root,INT_MIN);
        return ans;
    }
};