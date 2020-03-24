class Solution:
    def romanToInt(self, s: str) -> int:
        sym_int=[
            ("I",1),
            ("IV",4),
            ("V",5),
            ("IX",9),
            ("X",10),
            ("XL",40),
            ("L",50),
            ("XC",90),
            ("C",100),
            ("CD",400),
            ("D",500),
            ("CM",900),
            ("M",1000)            
        ]
        sym_int=dict(sym_int)
        result=0
        for i,v in enumerate(s):
            if i+1>= len(s):
                result+=sym_int[v]
            else:
                if sym_int[s[i+1]]>sym_int[v]:
                    result = result - sym_int[v]
                else:
                    result += sym_int[v]
        return result
                
            
            