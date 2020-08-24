class Solution:
    def __init__(self):
        self.memory={}
    
    def isMatch(self, s: str, p: str) -> bool:
        self.memory[(0,0)]=True
        for i in range(1,len(s)+1):
            self.memory[(i,0)]=False
        for i in range(1,len(p)+1):
            if p[i-1]=="*":
                self.memory[(0,i)]=self.memory[(0,i-2)]
            else:
                self.memory[(0,i)]=False
        return self.dp(len(s),len(p),s,p)
    
    def dp(self,i,j,s,p):
        if i<0 or j<0:
            return False
        key=(i,j)
        if key in self.memory:
            return self.memory.get(key)
        if p[j-1]=="*":
            if p[j-2] != s[i-1] and p[j-2] != ".":
                ans = self.dp(i,j-2,s,p)
            else:
                ans = self.dp(i-1,j,s,p) or self.dp(i,j-2,s,p)
            self.memory[key] = ans
            return ans
        else:
            if p[j-1] == s[i-1] or p[j-1] == ".":
                ans = self.dp(i-1,j-1,s,p)
            else:
                ans = False
            self.memory[key] = ans
            return ans