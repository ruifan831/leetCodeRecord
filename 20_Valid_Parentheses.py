class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stacks = [None]
        paren_dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i in paren_dict:
                if paren_dict[i]!=stacks.pop():
                    return False
            else:
                stacks.append(i)
        return len(stacks) == 1