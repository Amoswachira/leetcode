class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        B = []
        while k:
            a = num.pop() if num else 0
            k += a
            k, r = divmod(k, 10)
            B.append(r)
        B.reverse()
        return num+B
        