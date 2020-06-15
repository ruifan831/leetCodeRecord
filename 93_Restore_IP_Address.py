class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res=[]
        self.dfs([],s,0)
        return self.res
        
        
    def dfs(self,path,s,index):
        if len(path)==4:
            if index==len(s):
                self.res.append(".".join(path))
            return
        for i in range(1,4):
            if index+i >len(s):
                break
            if s[index]=="0" and i!=1:break
            char = s[index:index+i]

            if int(char)<=255:
                path.append(char)
                self.dfs(path,s,index+i)
                path.pop()
            
        