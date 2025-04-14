class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #brute force
        def merge(start,stop,mid):
            count = 0
            j = mid+1
            k=0
            temp = [0]*(stop-start+1)
            for i in range(start, mid + 1):
                while j <= stop and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            i,j = start,mid+1
            while i<=mid and j<=stop:
                if nums[i] > nums[j]:
                    # count+=(mid-i+1)
                    temp[k] = nums[j]
                    j+=1
                    k+=1
                else:
                    temp[k] = nums[i]
                    i+=1
                    k+=1
            
            while i<=mid:
                temp[k] = nums[i]
                k+=1
                i+=1
            while j<=stop:
                temp[k] = nums[j]
                k+=1
                j+=1

            k = 0
            for ind in range(start,stop+1):
                nums[ind]=temp[k]
                k+=1
            return count
        def mergeSort(start,stop):
            if start >= stop:
                return 0
            mid = (start+stop)//2
            count = mergeSort(start,mid)
            count+=mergeSort(mid+1,stop)
            count+= merge(start,stop,mid)
            return count
        return mergeSort(0,len(nums)-1)

        


                     

        



        
        