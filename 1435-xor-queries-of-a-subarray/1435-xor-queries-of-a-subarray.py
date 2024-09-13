class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        n = len(arr)
        prefix_xor = [0]*(n+1)
        for i in range(1,n+1):
            prefix_xor[i] = arr[i-1]^prefix_xor[i-1]
        # print(prefix_xor)
        for i, j in queries:
            curr_xor = prefix_xor[j+1]^prefix_xor[i]
            answer.append(curr_xor)

        return answer