class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        int_to_str = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        result=[]
        def helper(string,remain_digits):
            if len(remain_digits) == 0:
                result.append(string)
            else:
                for i in int_to_str[remain_digits[0]]:
                    helper(string+i,remain_digits[1:])
        if digits:
            helper("",digits)
        return result
        
        