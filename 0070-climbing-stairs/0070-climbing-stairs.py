class Solution:
    def climbStairs(self, n):
        if n < 2:
            return 1
        return self.tailRec(n, 1, 2)
        
    def tailRec(self, n, acc1, acc2):
        if n < 2:
            return acc1
        return self.tailRec( n - 1, acc2, acc1 + acc2)
        