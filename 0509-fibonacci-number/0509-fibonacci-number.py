class Solution:
    
    memo = {}
    
    def fib(self, N):
        self.memo = {}
        return self.helper(N)
    
    def helper(self,N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N in self.memo:
            return self.memo[N]
        
        n = self.helper(N-1) + self.helper(N-2)
        
        self.memo[N] = n
        return n
        