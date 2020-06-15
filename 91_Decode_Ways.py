class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        opt=[None]*(len(s)+1)
        opt[0],opt[1]=1,1
        for i in range(2,len(s)+1):
            if s[i-1] != "0" and s[i-2]!="0" :
                if int(s[i-2:i]) <= 26:
                    opt[i]=opt[i-1]+opt[i-2]
                else:
                    opt[i]=opt[i-1]   
            elif s[i-1] == "0" and s[i-2]=="0":
                return 0
            elif s[i-2] =="0":
                opt[i]=opt[i-1]
            else:
                if int(s[i-2:i]) <= 26:
                    opt[i]=opt[i-2]
                else:
                    return 0
        return opt[-1]
            