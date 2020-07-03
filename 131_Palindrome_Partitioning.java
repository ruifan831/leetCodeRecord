class Solution {
    private List<List<String>> res= new ArrayList<List<String>>();
    public List<List<String>> partition(String s) {
        System.out.println(s.substring(3));
        List<String> path_ = new ArrayList<String>();
        helper(s,path_);
        return res;
    }
    
    private void helper(String s, List<String> path){
        if (s.length() == 0){
            List<String> temp = new ArrayList<String>(path);
            res.add(temp);
        }
        for (int i=0;i<s.length();i++){
            String cur = s.substring(0,i+1);
            if (checkPalindrome(cur)){
                path.add(cur);
                helper(s.substring(i+1),path);
                path.remove(path.size()-1);
            }
        }
    }
    
    private Boolean checkPalindrome(String s){
        int start = 0, end =s.length()-1;
        while (start<end){
            if (s.charAt(start) != s.charAt(end)) return false;
            start+=1;
            end-=1;
        }
        return true;
    }
}