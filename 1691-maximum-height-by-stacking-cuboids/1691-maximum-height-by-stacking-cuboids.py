class Solution:
     def maxHeight(self, A):
        A = [[0, 0, 0]] + sorted(map(sorted, A))
        dp = [0] * len(A)
        for j in range(1, len(A)):
            for i in range(j):
                if all(A[i][k] <= A[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)