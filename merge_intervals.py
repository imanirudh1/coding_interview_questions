intervals = [[1,3],[2,6],[8,10],[15,18]]
def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals_sorted = sorted(intervals,key = lambda x: x[0])
    ans = []
    cur = intervals_sorted[0]
    for i in range(0,len(intervals)-1):
        if intervals_sorted[i+1][0] <= cur[1]:
            cur[1] = max(intervals_sorted[i+1][1],cur[1])
        else:
            ans.append(cur)
            cur = intervals_sorted[i+1]
    ans.append(cur)
    return ans
                     
print(merge(intervals))    