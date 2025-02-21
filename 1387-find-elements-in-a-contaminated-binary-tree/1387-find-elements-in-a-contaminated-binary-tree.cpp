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
class FindElements {
public:
    vector<int> inorder;
    void helper(TreeNode* root,int val){
        if(root==nullptr){
            return;
        }
        inorder.push_back(val);
        if(root->left){
            helper(root->left,val*2+1);
        }
        if(root->right){
            // root->right->val = 2*root->val+2;
            helper(root->right,val*2+2);
        }
        return;
    }
    FindElements(TreeNode* root) {
        helper(root,0);
    }
    bool find(int target) {
        return std::find(inorder.begin(),inorder.end(),target)!=inorder.end();
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */