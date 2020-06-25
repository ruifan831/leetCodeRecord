class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int buyPoint = Integer.MAX_VALUE;
        for (int i: prices){
            if (i<buyPoint){
                buyPoint=i;
            } else{
                profit += (i-buyPoint);
                buyPoint = i;
                
            }
        }
        return profit;
    }
}
