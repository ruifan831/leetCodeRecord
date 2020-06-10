from collections import defaultdict
class Solution:
    # set two pointers to keep track of the current sub string
    # Construct a dictionary to store the maximum times each characters require
    def minWindow(self, s: str, t: str) -> str:
        str_count=defaultdict(int)
        for i in t:
            str_count[i] +=1
        p1,p2=0,len(s)
        contain = 0
        result=""
        min_length = float("inf")
        # keep increment the pointer 2
        # Update the dictionary everytime we saw the required character
        # Create a variable "contain" to store the number of required charcters have seen
        # Only increment the "contain" if the current char is in the dictionary and the corresponding value is greater than 0.
        # everytime before we increment the pointer 2, check if we can increment pointer 1
        # and sub string still contains the targer string.
        # Also update the result if the sub string is shorter than previous result.
        for i in range(p2):
            if s[i] not in str_count:
                continue
            str_count[s[i]] -=1
            if str_count[s[i]] >=0:
                contain+=1
            while contain == len(t):
                char = s[p1]
                
                cur_result = s[p1:i+1]
                if len(cur_result)<min_length:
                    result=cur_result
                    min_length=len(cur_result)
                
                p1+=1
                if char in str_count:
                    str_count[char]+=1
                    if str_count[char]>0:
                        contain-=1
        return result
                    
                    
            
            
                