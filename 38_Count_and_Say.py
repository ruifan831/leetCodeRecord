class Solution:
    # Recursive
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n-1)
        ns = ""
        count = 1
        for i in range(len(prev)-1):
            if prev[i] == prev[i+1]:
                count+=1
            else:
                ns += str(count)+prev[i]
                count = 1
        ns += str(count)+prev[-1]
        return ns
    
    # Iterative
    def countAndSay1(self, n: int) -> str:
        result = "1"
        if n == 1:
            return "1"
        while n > 1:
            ns = ""
            count = 1
            for i in range(len(result)-1):
                if result[i] == result[i+1]:
                    count+=1
                else:
                    ns += str(count)+result[i]
                    count = 1
            ns += str(count)+result[-1]
            n-=1
            result = ns
        return result
        