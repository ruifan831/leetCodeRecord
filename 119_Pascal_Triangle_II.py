class Solution {
    public List<Integer> getRow_2(int rowIndex) {
        Integer[] res = new Integer[rowIndex+1];
        Arrays.fill(res,0);
        res[0]=1;
        for (int i =1; i<= rowIndex;i++){
            for (int j=i;j>0;j--){
                res[j] = res[j]+res[j-1];
            }
        }
        return Arrays.asList(res);
    }
    
    public List<Integer> getRow(int rowIndex) {
        List<Integer> pre = Arrays.asList(1);
        if (rowIndex == 0) return pre;
        for (int i=2; i<=rowIndex+1;i++){
            List<Integer> cur = new ArrayList<Integer>();
            cur.add(1);
            for (int j=1;j<i-1;j++){
                cur.add(pre.get(j-1)+pre.get(j));
            }
            cur.add(1);
            pre = cur;
        }

        return pre;
        
    }
}