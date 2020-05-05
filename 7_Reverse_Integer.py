class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            temp=int(str(x*(-1))[::-1])
        else:
            temp=int(str(x)[::-1])
            
        if temp>pow(2,31):
            return 0
        else:
            if x<0:
                return temp*-1
            else:
                return temp