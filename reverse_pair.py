cnt=0
def reversePairs(nums):   
    def msort(lst):
        L = len(lst)
        if L <= 1:                          # base case
            return lst
        else:                               # recursive case
            return merger(msort(lst[:int(L/2)]), msort(lst[int(L/2):]))
    def merger(left, right):
        # merger
        global cnt
        l, r = 0, 0                         # increase l and r iteratively
        while l < len(left) and r < len(right):
            if left[l] <= 2*right[r]:
                l += 1
            else:
                cnt += len(left)-l     # add here
                r += 1
        return sorted(left+right)           # I can't avoid TLE without timsort...
    msort(nums)
    return cnt

print(reversePairs([2,4,3,5,1]))