class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip().split("/")
        stack = []
        # Using stack and add directory to the stack if the directory is not ".", ".." or "".
        # pop out the last element if ".." was seen.
        for i in path:
            if i == ".." and stack:
                stack.pop()
            elif (i != "." and  i!="" and i!=".."):
                stack.append(i)
        
        return "/"+"/".join(stack)