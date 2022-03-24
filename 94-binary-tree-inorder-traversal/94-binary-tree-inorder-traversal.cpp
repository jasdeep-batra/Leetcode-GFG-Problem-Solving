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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode* prev = nullptr;
        while(root)
        {
            if(root->left)
            {
                prev = root->left;
                while(prev->right!=nullptr && prev->right!=root)
                {
                    prev=prev->right;
                }
                if(prev->right==nullptr)
                {
                    prev->right = root;
                    root=root->left;
                }
                else
                {
                    prev->right=NULL;
                    result.push_back(root->val);
                    root = root->right;
                }
            }
            else
            {
                result.push_back(root->val);
                root=root->right;
            }
        }
        return result;
    }
};