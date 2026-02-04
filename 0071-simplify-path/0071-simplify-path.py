class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip('/')
        directory = path.split('/')
        print(directory)
        stack = []
        for item in directory:
            if item == '..':
                if stack:
                    stack.pop()
            elif item=='.':
                continue
            elif item!='':
                print(item)
                if item[0]=='/':
                    stack.append(item[1:])
                else:
                    stack.append(item)
        ans = "/"
        for item in stack:
            ans+=item+'/'

        return ans[:-1] if ans!='/' else ans