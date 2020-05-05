class Solution:
    def lengthOfLongestSubstring(self, s):
        char_pos=dict()
        global_max=0
        current_max=0
        start_pos=0
        for index,i in enumerate(s):
            if i in char_pos and char_pos[i] >= start_pos:
                start_pos = char_pos[i] + 1
                current_max= index - start_pos+1
                global_max=max(global_max,current_max)
                char_pos[i]=index
            else:
                char_pos[i]=index
                current_max +=1
                global_max=max(global_max,current_max)
        return global_max
                