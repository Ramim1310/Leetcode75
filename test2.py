class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result=""
        minSize=min(len(word1),len(word2))
        
        for i in range(minSize):
            result=result+word1[i]+word2[i]
            
        result=result+word1[minSize:]+word2[minSize:]
        
        
        
        return result
    
test=Solution()

result=test.mergeAlternately('abcd','ab')  

print(result)