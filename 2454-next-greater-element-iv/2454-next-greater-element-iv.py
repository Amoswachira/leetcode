class Solution:
    def secondGreaterElement(self, A: List[int]) -> List[int]:
        mid, stk, n = [[] for _ in range(len(A))], [], len(A)
        for i in range(n):
            while stk and A[stk[-1]] < A[i]:
                mid[i].append(stk.pop())
            stk.append(i)
        pq, ans = [], [-1] * len(A)
        for i in range(n):
            while pq and pq[0][0] < A[i]:
                ans[heappop(pq)[1]] = A[i]
            for j in mid[i]:
                heappush(pq, (A[j], j))
        return ans