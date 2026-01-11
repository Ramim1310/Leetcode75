class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result=[]
        minSize=min(len(word1),len(word2))
        
        for i in range(minSize):
            result.append(word1[i]+word2[i])
            
        result.append(word1[minSize:]+word2[minSize:])
        
        
        
        return "".join(result)
    
test=Solution()

result=test.mergeAlternately('abcd','p')  

print(result)