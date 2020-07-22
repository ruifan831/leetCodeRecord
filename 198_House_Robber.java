class Solution {
    public int rob(int[] nums) {
        if (nums.length ==0) return 0;
        int[] opt = new int[nums.length+1];
        opt[1] = nums[0];
        opt[0] = 0;
        for(int i =2;i<=nums.length;i++){
            opt[i]=Math.max(opt[i-1],opt[i-2]+nums[i-1]);
        }
        return opt[opt.length-1];
        
    }
}