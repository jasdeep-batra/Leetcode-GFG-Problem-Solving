class Solution {
public:
    vector<int> res;
    vector<bool> used;
    
    bool backtrack(int idx, int n) {
        if (idx == res.size()) {
            return true;
        }
        if (res[idx] != 0) {
            return backtrack(idx + 1, n);
        }
        
        for (int num = n; num >= 1; num--) {
            if (used[num]) continue;

            int secondIdx = (num == 1) ? idx : idx + num;
            if (secondIdx < res.size() && res[secondIdx] == 0) {
                res[idx] = res[secondIdx] = num;
                used[num] = true;

                if (backtrack(idx + 1, n)) return true;
                
                res[idx] = res[secondIdx] = 0;
                used[num] = false;
            }
        }
        return false;
    }

    vector<int> constructDistancedSequence(int n) {
        res.resize(2 * n - 1, 0);
        used.resize(n + 1, false);
        
        backtrack(0, n);
        return res;
    }
};
