class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        num1,count1 = 0,0
        num2,count2 = 0,0

        for item in nums:
            if item==num1:
                count1+=1
            elif item==num2:
                count2+=1 
                
            elif count1==0:
                num1 = item 
                count1+=1 
                     
            elif count2==0:
                num2 = item
                count2+=1
            else:
                count2-=1
                count1-=1
        
        count1,count2=0,0
        for item in nums:
            if item==num1:
                count1+=1
            elif item==num2:
                count2+=1

        ans = []
        if count1 > (n//3):
            ans.append(num1)
        if count2 > (n//3):
            ans.append(num2)
        # print(num1,"fuck",num2)
        return ans


        

        