class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0 or len(s)==1:
            return s
        opt=[[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            opt[i][i]=True
            if i>0:
                opt[i][i-1]=True
        ans=s[0]
        for i in range(len(s)-1)[::-1]:
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if opt[i+1][j-1]:
                        ans=s[i:j+1] if len(s[i:j+1]) > len(ans) else ans
                        opt[i][j]=opt[i+1][j-1]
                    else:
                        opt[i][j]=opt[i+1][j-1]
                else:
                    opt[i][j]=False
        return ans
        