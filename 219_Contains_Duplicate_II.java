class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer,Integer> dict = new HashMap<Integer,Integer>();
        for (int i=0;i<nums.length;i++){
            if (dict.containsKey(nums[i])){
                if (Math.abs(dict.get(nums[i])-i)<=k) return true;
            }
            dict.put(nums[i],i);
        }
        return false;
    }
}