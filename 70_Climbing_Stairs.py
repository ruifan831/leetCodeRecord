class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        self.opt = [None]*(n+1)
        self.opt[1]=1
        self.opt[2]=2
        return self.helper(n)
    # there is only two ways to reach step n
    # one is taking one step from n-1 to n
    # the other is taking two steps from n-2 to n
    # Hence, number of way to reach n is the sum of number of ways reach to n-1 and n-2
    def helper(self,n):
        if self.opt[n]:
            return self.opt[n]
        else:
            self.opt[n]=self.helper(n-1)+self.helper(n-2)
            return self.opt[n]
    
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        oneStepBefore=1
        twoStepBefore=1
        for i in range(2,n+1):
            twoStepBefore,oneStepBefore=oneStepBefore,oneStepBefore + twoStepBefore
        return oneStepBefore
            
            
        
    
        