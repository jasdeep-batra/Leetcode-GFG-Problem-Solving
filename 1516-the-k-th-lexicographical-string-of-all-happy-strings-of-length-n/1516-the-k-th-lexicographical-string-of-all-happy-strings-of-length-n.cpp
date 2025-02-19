class Solution {
public:
    vector<string> res;
    vector<int> visit;
    vector<char> arr;

    void helper(int n, string s,int k){
        if (s.size() == n){
            res.push_back(s);
            return;
        }
        for (int i = 0; i < 3; i++){
            if (s.empty() || s.back() != arr[i]){
                helper(n, s + arr[i],k);
                if(res.size()==k){
                    break;
                }
            }
        }
        
    }

    string getHappyString(int n, int k) {
        arr = {'a', 'b', 'c'};
        visit.resize(3, 0);
        helper(n, "",k);
        return (k <= res.size()) ? res[k - 1] : "";
    }
};
