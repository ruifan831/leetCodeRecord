
class Solution:
    def numTrees(self, n: int) -> int:
        opt=[1,1]
        for i in range(2,n+1):
            p1=0
            p2=i-1
            result=0
            while p1<i and p2>=0:
                result += opt[p1]*opt[p2]
                p1+=1
                p2-=1
            opt.append(result)
        return opt[n]
