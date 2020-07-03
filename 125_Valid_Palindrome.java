import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Solution {
    public boolean isPalindrome_2(String s) {
        int st = 0;
        int e = s.length()-1;
        while (st<e){
            if (!Character.isLetterOrDigit(s.charAt(st)) || !Character.isLetterOrDigit(s.charAt(e))){
                if (!Character.isLetterOrDigit(s.charAt(st))) st+=1;
                if (!Character.isLetterOrDigit(s.charAt(e))) e-=1;
            } else{
                if (Character.toLowerCase(s.charAt(st)) != Character.toLowerCase(s.charAt(e))){
                    return false;
                } else {
                    st+=1;
                    e-=1;
                }
            }
            
        }
        return true;
    }
    public boolean isPalindrome(String s) {
        String pattern = "\\W*";
        Pattern p = Pattern.compile(pattern);
        Matcher m = p.matcher(s); 
        s = m.replaceAll("").toLowerCase();
       
        int st = 0;
        int e = s.length()-1;
        while (st<e){
            if (s.charAt(st) !=s.charAt(e)) return false;
            st+=1;
            e-=1;
        }
        return true;
    }
}