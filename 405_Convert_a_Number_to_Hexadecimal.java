class Solution {
    public String toHex(int num) {
        
        if (num>=0 & num<10){
            return Integer.toString(num);
        } else if(num<16 & num>=0){
            return Character.toString('a'+num-10);
        }
        return toHex(num>>>4)+toHex(num&15);
    }
}