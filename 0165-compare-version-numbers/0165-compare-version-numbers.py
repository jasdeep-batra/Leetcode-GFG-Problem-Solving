class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        print(v2)
        print(len(v1))
        for i in range(len(v1)):
            # print(int(v1[i]),int(v2[i]))
            if i>=len(v2):
                if int(v1[i]) > 0:
                    return 1
            elif int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                print("enter")
                return -1
        if len(v2) > len(v1):
            for i in range(len(v1),len(v2)):
                if int(v2[i]) > 0:
                    return -1
        
        return 0
        
