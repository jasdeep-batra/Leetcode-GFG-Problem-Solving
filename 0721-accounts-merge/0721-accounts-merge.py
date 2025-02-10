from sortedcontainers import SortedList
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}  #email to parent of email
        names = {}  #email to name
        accounts.sort()
        def find(email):
            if email not in parent:
                parent[email] = email
            if parent[email]!=email:
                parent[email] = find(parent[email])
            return parent[email]

        def union(email1, email2):
            pass
        for account in accounts:
            name = account[0]
            emails = account[2:]

            first_email = account[1]
            pa1 = find(first_email)
            for email in emails:
                print(email)
                pa2 = find(email)
                parent[pa2] = pa1
            if pa1 not in names:
                names[pa1] = [name,set([])]

        for sub,sup in parent.items():
            names[find(sup)][1].add(sub)

        res = []
        for key,value in names.items():
            if len(value[1])==0:
                continue
            t2 = list(value[1])
            t2.sort()
            temp = [value[0]]+t2
            res.append(temp)
        return res

        

        








        

        