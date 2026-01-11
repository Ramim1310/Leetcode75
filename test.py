class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        i= len(digits)-1
        
        while i>=0:
            if digits[i]<9:
                digits[i]+=1
                return digits  
            else:
                digits[i]=0
                i-=1
                
        return [1]+digits
            
            
        
        
        
 
test = Solution() 

result = test.plusOne([9,9,9])
print(result)  
