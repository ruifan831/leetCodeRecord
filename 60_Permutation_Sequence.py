class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.res=[]
        self.used = [False]*n
        starting_root = (k-1)//math.factorial(n-1)
        self.used[starting_root] = True
        self.dfs(1,[starting_root+1],n)
        return "".join([str(i) for i in self.res[(k-1)%math.factorial(n-1)]])
    
    def dfs(self,level,path,n):
        if level == n:
            self.res.append(path[:])
            return
        for i in range(1,n+1):
            if self.used[i-1]:
                continue
            path.append(i)
            self.used[i-1] = True
            self.dfs(level+1,path,n)
            path.pop()
            self.used[i-1] = False
        return
            
class Solution_2:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        candidates = [i for i in range(1,n+1)]
        k -= 1
        while candidates:
            # We wanna find out the starting index of kth permutation sequence for current all possiblt N permutation.
            # Then add the number to result, and update N by minus 1
            # Update k by finding the remainder of K/(N-1)!, 
            # since we know the final result will be the cuurent staring number + new kth permutation sequence of the next all possible N-1 permutations.
            starting_root = k//math.factorial(n-1)
            res.append(str(candidates.pop(starting_root)))
            print(candidates)
            k = k%math.factorial(n-1)
            n -= 1
        return "".join(res)