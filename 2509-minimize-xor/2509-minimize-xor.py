class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        sett = bin(num2).count('1')
        ans = 0
        
        # Step 1: Use the set bits in num1
        for i in range(31, -1, -1):  # Iterate from the most significant bit to the least
            if sett == 0:  # Stop if we have used all the needed bits
                break
            if (num1 >> i) & 1:  # Check if the i-th bit in num1 is set
                ans |= (1 << i)  # Set the i-th bit in ans
                sett -= 1
        
        # Step 2: Add remaining bits from the least significant position
        for i in range(32):  # Iterate from the least significant bit to the most
            if sett == 0:  # Stop if we have used all the needed bits
                break
            if not (ans >> i) & 1:  # Check if the i-th bit in ans is not set
                ans |= (1 << i)  # Set the i-th bit in ans
                sett -= 1

        return ans
