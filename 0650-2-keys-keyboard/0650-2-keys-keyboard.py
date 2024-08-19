class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        self.target_length = n
        self.cache = [[-1] * (n // 2 + 1) for _ in range(n + 1)]
        
        def calculate_min_ops(current_length: int, clipboard_length: int) -> int:
            if current_length == self.target_length:
                return 0
            if current_length > self.target_length:
                return float('inf')
            
            if self.cache[current_length][clipboard_length] != -1:
                return self.cache[current_length][clipboard_length]
            
            paste_option = 1 + calculate_min_ops(current_length + clipboard_length, clipboard_length)
            copy_paste_option = 2 + calculate_min_ops(current_length * 2, current_length)
            
            result = min(paste_option, copy_paste_option)
            self.cache[current_length][clipboard_length] = result
            return result
        
        return 1 + calculate_min_ops(1, 1)