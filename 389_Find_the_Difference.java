class Solution {
    public char findTheDifference(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i=0;i<s.length();i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        for (int i=0;i<t.length();i++){
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) - 1);
        }
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey());
            System.out.println(entry.getValue());
            if (entry.getValue()==-1){
                return entry.getKey();
            }
        }
        return 'a';
    }

    public char findTheDifference_2(String s, String t) {
        char res = t.charAt(t.length()-1);
        for (int i =0 ; i <s.length();i++){
            res ^= s.charAt(i);
            res ^= t.charAt(i);
        }
        return res;
        
    }
}