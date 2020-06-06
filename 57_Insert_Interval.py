# O(NlogN)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)
    
    def merge(self, intervals):
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

# O(N)
class Solution_2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        # keep updating newInterval until it does not overlap with any interlval in the list
        for i,cur in enumerate(intervals):
            if cur[1]<newInterval[0]:
                result.append(cur)
            elif cur[0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval[0] = min(cur[0],newInterval[0])
                newInterval[1] = max(cur[1],newInterval[1])
        result.append(newInterval)
        return result
                