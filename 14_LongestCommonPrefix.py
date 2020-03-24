# Using Divide and Conquer
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        def commonWordBetweenTwoWords(l_str,r_str):
            longest_prefix= min(len(l_str),len(r_str))
            i=0
            while i<longest_prefix:
                if l_str[i] != r_str[i]:
                    break
                i+=1
            return l_str[0:i]
        
        def help_recursion(str_list,start,end):
            if start >= end:
                return strs[start]
            else:
                mid_point= (start+end)//2
                left= help_recursion(str_list,start,mid_point)
                right= help_recursion(str_list,mid_point+1,end)
                return commonWordBetweenTwoWords(left,right)
        if len(strs) == 0:
            return ""
        else:
            return help(strs,0,len(strs)-1)
                
            
            