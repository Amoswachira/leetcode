class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total_sum = 0
            while num > 0:
                num , digit = divmod(num,10)
                total_sum += digit ** 2
            return total_sum
        
        seen = set()
        while n != 0 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
        