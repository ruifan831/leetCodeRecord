class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(o,c,start_string):
            if o ==0 and c ==0:
                res.append(start_string)
            if o>0:
                generate(o-1,c,start_string+"(")
            if c>0 and o<c:
                generate(o,c-1,start_string+")")
        generate(n,n,"")
        return res

    def generateParenthesis1(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        result = []
        for i in range(n):
            for j in self.generateParenthesis1(i):
                for k in self.generateParenthesis1(n-1-i):
                    print(k)
                    result.append("({}){}".format(j,k))
        return result