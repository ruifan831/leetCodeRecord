class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res=[]
        cur=[]
       
        for i in range(len(intervals)):
            if i == 0:
                cur = intervals[i]
                i+=1
                continue
            if cur[1] >= intervals[i][0]:
                cur[1] = max(cur[1],intervals[i][1])
            else:
                res.append(cur)
                cur = intervals[i]

        res.append(cur)
        return res