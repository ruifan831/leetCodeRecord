class Solution {
    public int titleToNumber(String s) {
        int res= 0;
        for (int i=0;i<s.length();i++){
            int cur= s.charAt(i)-'A'+1;
            if (i==s.length()-1){
                res+=cur;
            } else{
                res+=Math.pow(26,s.length()-i-1)*cur;
            }
        }
        return res;
    }
}