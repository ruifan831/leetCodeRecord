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
}