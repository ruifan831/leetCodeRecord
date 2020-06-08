class Solution:
    # opt[m][n] is the minimum edit distance required for word1[:m+1] and word2[:n+1]
    # if word1[m] == word2[n]: opt[m][n] = opt[m-1][n-1]
    # else:
    #       1: replace a character opt[m][n] = opt[m-1][n-1] + 1
    #       2: delete a character from word1 opt[m][n] = opt[m-1][n] + 1
    #       3: insert a charcter to word1 opt[m][n] = opt[m][n-1] + 1
    #       opt[m][n] = minimum of above 3 cases.
    # Since we add a padding for opt, when we consider the solution at position (m,n)
    # We are checking the char of word1[m-1] and word2[n-1]
    #           null    h   o   r   s   e
    #   null      0     1   2   3   4   5
    #   r         1     N   N   N   N   N
    #   o         2     N   N   N   N   N
    #   s         3     N   N   N   N   N
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1=word1
        self.word2=word2
        self.opt=[[None]*(len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(word2)+1):
            self.opt[0][i] = i
        for i in range(len(word1)+1):
            self.opt[i][0] = i
        return self.helper(len(word1),len(word2))

        
    def helper(self,m,n):
        if self.opt[m][n] is not None:
            return self.opt[m][n]
        if self.word1[m-1] == self.word2[n-1]:
            self.opt[m][n]=self.helper(m-1,n-1)
        else:
            self.opt[m][n]=min(self.helper(m-1,n-1)+1,self.helper(m,n-1)+1,self.helper(m-1,n)+1)
        return self.opt[m][n]
            
        
            