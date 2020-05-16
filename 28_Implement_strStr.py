class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        p2 = 0
        while p2<len(needle) and p1< len(haystack):
            if haystack[p1] == needle[p2]:
                p1+=1
                p2+=1
            else:
                p1-=p2-1
                p2=0
            print(p2)
        if p2< len(needle):
            return -1
        else:
            return p1-p2
    def strStr2(self, haystack: str, needle: str) -> int:
        if haystack == needle: return 0
        span_length = len(needle)
        for i in range(len(haystack)-span_length+1):
            if haystack[i:i+span_length] == needle:
                return i
        return -1
                