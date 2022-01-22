#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
        first = 0
        last = len(arr)-1
        index = -1
        while first <= last:
            mid = first + (last-first)//2
            if(arr[mid]==1):
                index = mid
                last = mid-1
            elif(arr[mid]==0):
                first = mid+1
        return index



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends