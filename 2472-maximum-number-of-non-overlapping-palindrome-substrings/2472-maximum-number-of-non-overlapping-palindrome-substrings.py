class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        def pal(i, j):
            if i < 0 : return False
            return s[i:j] == s[i:j][::-1]
        
        dp = [0] * (len(s)+1)
        
        for i in range(k, len(s)+1):
            dp[i] = dp[i-1]
            if pal(i-k,i)   : dp[i] = max(dp[i], 1 + dp[i-k])
            if pal(i-k-1,i) : dp[i] = max(dp[i], 1 + dp[i-k-1])
        
        return dp[-1]