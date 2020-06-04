class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.helper(x,abs(n))
        print(type(result))
        if n<0:
            return max(-1<<32,1/result)
        else:
            return min(1<<32-1,result)
    def helper(self,x,n):
        if n == 0:
            return 1.0
        y = self.helper(x,n//2)
        if n%2==1:
            return x*y*y
        else:
            return y*y

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        neg = False
        if n<0:
            neg = True
        n= abs(n)
        remainder = 1
        # update x while divide n by 2.
        # everytime before we dived n, have to check if n is divisble by 2.
        # if not, we need to update the remainder by mutiply current x.
        while n>1:
            if n%2 == 1:
                remainder *= x
            n= n>>1
            x*=x
        x= x*remainder
        if neg:
            return max(-1<<32,1/x)
        else:
            return min(1<<32-1,x)
            
            
 