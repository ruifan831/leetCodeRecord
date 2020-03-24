import re
class Solution:
    def myAtoi(self, str: str) -> int:
        stripped_result=str.strip()
        patterns=re.compile("^[+-]{0,1}[\d]+")
        temp=patterns.match(stripped_result)
        if temp:
            result = int(temp.group(0))
            maxi=2**31
            if result < maxi and result >= -maxi:
                return result
            elif result >= maxi:
                return maxi-1
            else:
                return -maxi
        else:
            return 0