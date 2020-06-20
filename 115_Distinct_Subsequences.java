class Solution {
    private int res = 0;
    public int numDistinct(String s, String t) {
        dfs(0,0,s,t);
        return res;
    }
    
    private void dfs(int index_t,int index_s,String s, String t){
        if (index_t == t.length()){
            res+=1;
            return ;
        }
        for (int i = index_s;i<s.length();i++){
            if (s.charAt(i) == t.charAt(index_t)){
                dfs(index_t+1,i+1,s,t);
            }
        }
        
    }
    // opt[i][j] is number of distinct ways for s[0,j] and t[0,i]
    // if s[j] == t[i]:
    //      opt[i][j] = opt[i-1][j-1] + opt[i][j-1]
    // opt[i-1][j-1] is number of distinct ways without considering s[j] and t[i]
    // opt[i][j-1] is find the number of distinct ways between s[0,j-1] and t[0,i]
    public int numDistinct_DP(String s, String t) {
        int[][] opt = new int[t.length()+1][s.length()+1];
        for (int i = 0;i<=s.length();i++){
            opt[0][i]=1;
        }
        for (int i = 1;i<=t.length();i++){
            opt[i][0]=0;
        }
        for (int i = 0;i<t.length();i++){
            for (int j=0;j<s.length();j++){
                opt[i+1][j+1] = opt[i+1][j];
                if (s.charAt(j)==t.charAt(i)){
                    opt[i+1][j+1]+=opt[i][j];
                }
            }
        }
        return opt[t.length()][s.length()];
    }
}