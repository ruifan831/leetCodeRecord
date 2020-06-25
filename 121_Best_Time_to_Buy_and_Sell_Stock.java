class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int minPoint = Integer.MAX_VALUE;
        for (int i: prices){
            if (i<minPoint) {
                minPoint = i;
            } else if((i-minPoint)>max){
                max= i-minPoint;
            }
        }
        return max;
    }
}
