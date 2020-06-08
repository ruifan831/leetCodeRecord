class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        l,r=0,x
        while r>l:
            m=(l+r)//2
            if m**2<=x and x<(m+1)**2:
                return m
            elif m**2>x:
                r=m
            else:
                l=m
        
        
        