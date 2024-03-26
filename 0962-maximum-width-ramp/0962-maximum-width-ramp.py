class Solution:
    def maxWidthRamp(self, A):
        ind, mx, index = float("inf"), 0, collections.defaultdict(list)
        for i, num in enumerate(A):
            index[num].append(i)
        for num in sorted(A):
            mx = max(mx, index[num][-1] - ind)
            ind = min(ind, index[num][0])
        return mx