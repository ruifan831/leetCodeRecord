class Solution {
    public String countAndSay(int n) {
        if (n == 1){
            return "1";
        } else {
            String prev = countAndSay(n-1);
            String new_string = "";
            int count = 1;
            for (int i = 0; i < prev.length()-1; i++) {
                if (prev.charAt(i) != prev.charAt(i+1)){
                    new_string += Integer.toString(count);
                    new_string += Character.toString(prev.charAt(i));
                    count = 1;
                } else{
                    count += 1;
                };
            };
            new_string += String.valueOf(count);
            new_string += Character.toString(prev.charAt(prev.length()-1));
            
            return new_string;
        }
        
    };
    
    
}