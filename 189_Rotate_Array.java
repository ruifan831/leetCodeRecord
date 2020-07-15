class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        if (k==0) return ;
        int temp=nums[nums.length-1];
        for (int i = 0;i<nums.length;i++){
            int cur = nums[i];
            nums[i]=temp;
            temp = cur;
        }
        rotate(nums,k-1);
    }
}s