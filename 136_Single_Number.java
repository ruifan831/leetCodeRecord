class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> dict = new HashMap<>();
        for (int i: nums){
            dict.put(i,dict.getOrDefault(i,0)+1);
        }
        for (Map.Entry mapElement : dict.entrySet()) {
            if ( (int)mapElement.getValue()== 1) return (int)mapElement.getKey();
        }
        return 0;
    }
}