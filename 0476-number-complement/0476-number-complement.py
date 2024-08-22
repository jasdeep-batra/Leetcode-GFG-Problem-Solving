class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Find the binary representation of num
        ans = ""
        original_num = num
        
        while num:
            # Get the least significant bit and append it
            ans = str(num & 1) + ans
            # Right shift num to continue
            num = num >> 1
        
        # Step 2: Flip the bits (complement the binary string)
        complement = ""
        for bit in ans:
            # Flip 1 to 0 and 0 to 1
            complement += '1' if bit == '0' else '0'
        
        # Step 3: Convert the complement back to an integer
        res = int(complement, 2)
        
        return res



        