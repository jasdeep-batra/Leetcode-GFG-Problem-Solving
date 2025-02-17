class Solution {
    public int numTilePossibilities(String tiles) {
        int[] count = new int[26]; // Frequency map for characters
        for (char c : tiles.toCharArray()) {
            count[c - 'A']++;
        }
        return helper(count);
    }

    private int helper(int[] count) {
        int sum = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] == 0) continue; // Skip if no more of this character is available
            sum++; // Count the current character as a sequence
            count[i]--; // Use one occurrence of the character
            sum += helper(count); // Recurse with the updated count
            count[i]++; // Backtrack: restore the character count
        }
        return sum;
    }
}