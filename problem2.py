class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_val=0
        ans=[]
        
        for i in candies:
            if i>max_val:
                max_val=i
        
        for i in candies:
            if i+extraCandies>=max_val:
                 ans.append(True)
            else:
                 ans.append(False)
        
        return ans
        
test=Solution()

result=test.kidsWithCandies([2,3,5,1,3],3)  

print(result)    