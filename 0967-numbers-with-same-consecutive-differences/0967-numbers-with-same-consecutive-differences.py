class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = list(range(10))
        for _ in range(N - 1):
            ans = [i * 10 + j for i in ans for j in {i % 10 - K, i % 10 + K} if i > 0 and 0 <= j < 10]
        return ans
        