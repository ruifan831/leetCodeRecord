class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        s,e=0,len(x)-1
        while s<e:
            if x[s]==x[e]:
                s+=1
                e-=1
            else:
                return False
        return True