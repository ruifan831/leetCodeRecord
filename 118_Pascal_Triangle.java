class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (numRows == 0) return res;
        List<Integer> pre = new ArrayList<Integer>();
        res.add(Arrays.asList(1));
        for (int i=2; i<=numRows;i++){
            List<Integer> cur = new ArrayList<Integer>();
            cur.add(1);
            for (int j=1;j<i-1;j++){
                cur.add(pre.get(j-1)+pre.get(j));
            }
            cur.add(1);
            pre = cur;
            res.add(cur);
        }

        return res;
    }
}