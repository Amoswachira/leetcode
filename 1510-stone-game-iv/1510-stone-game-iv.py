class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(n):
            if not n: return False
            return any(not dfs(n-i*i) for i in range(1, isqrt(n)+1)[::-1])
        return dfs(n)
        