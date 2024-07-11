class Solution:
    def reverseParentheses(self, s: str) -> str:
        #odd parenthesis then reverse else do not
        count = 0
        stack = deque()
        index_pair = [0 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                start = stack.pop()
                end = i
                index_pair[start] = end
                index_pair[end] = start

        ans = []
        curr_ind = 0
        direction = 1
        while curr_ind < len(s):
            if s[curr_ind] in "()":
                curr_ind = index_pair[curr_ind]
                direction*=-1
            else:
                ans.append(s[curr_ind])
            curr_ind+=direction
        return "".join(ans)

        