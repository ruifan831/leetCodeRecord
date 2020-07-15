class Solution {
    public String convertToTitle(int n) {
        if (n==0) return "";
        return convertToTitle((n-1)/26)+Character.toString('A'+(n-1)%26);
    }
} 