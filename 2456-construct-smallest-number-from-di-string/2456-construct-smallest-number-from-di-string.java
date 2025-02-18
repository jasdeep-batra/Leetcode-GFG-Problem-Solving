class Solution {
    public String smallestNumber(String pattern) {
        int n = pattern.length();
        boolean[] used = new boolean[10]; // Boolean array to track used digits
        StringBuilder res = new StringBuilder();
        
        backtrack(pattern, res, used, 0, n);
        
        return res.toString();
    }

    private boolean backtrack(String pattern, StringBuilder res, boolean[] used, int index, int n) {
        if (res.length() == n + 1) {
            return true; // Found the smallest valid number
        }

        for (int digit = 1; digit <= 9; digit++) {
            if (used[digit]) continue;

            // Ensure we respect 'I' (Increasing) and 'D' (Decreasing) pattern
            if (index == 0 || (pattern.charAt(index - 1) == 'I' && digit > res.charAt(res.length() - 1) - '0')
                || (pattern.charAt(index - 1) == 'D' && digit < res.charAt(res.length() - 1) - '0')) {

                used[digit] = true;
                res.append(digit);

                if (backtrack(pattern, res, used, index + 1, n)) {
                    return true; // Stop recursion once we find the smallest valid number
                }

                res.deleteCharAt(res.length() - 1);
                used[digit] = false;
            }
        }

        return false;
    }
}
