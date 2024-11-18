class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        #we can use prefix and suffix sum?
        if k==0:
            return [0]*len(code)

        new_code = code + code + code 
        n = len(code)
        if k > 0:
            for i in range(len(code)):
                # print(new_code[i+1:i+1+k])
                code[i] = sum(new_code[i+1:i+1+k])
        if k < 0:
            for i in range(len(code)):
                # print(new_code[n+i-1:n+i-1+k:-1])
                code[i] = sum(new_code[n+i-1:n+i-1+k:-1])
        return code

# 5 7 1 4 5 7 1 4 5 7 1 4 
        