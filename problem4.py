class Solution:
    def swap(self,arr,a,b):
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp
    def reverseVowels(self, s: str) -> str:
        arr=list(s)
        vowel=[]
        size_arr=len(arr)
        
        
       
        
        for i in range(size_arr):
            
            if arr[i]  in 'aeiou' or arr[i]  in 'AEIOU':
                vowel.append(i)
                
        size_vowel=len(vowel)    
        
        for i in range(size_vowel//2):
            self.swap(arr,vowel[i],vowel[size_vowel - i - 1])   
          
        return "".join(arr)  
    
    
    
test=Solution()

result=test.reverseVowels("leetcode")  

print(result)      





