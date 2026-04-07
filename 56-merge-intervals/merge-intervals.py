class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged =[intervals[0]]
        for strat, end in intervals[1:]:
            last_end = merged[-1][1]
            if strat <= last_end :
                merged[-1][1] = max(last_end , end)
            else:
                merged.append([strat,end])
        return merged