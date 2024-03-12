class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        idx = len(str(int(num[::-1]))) - len(num)
        
        return num[:idx] if idx < 0 else num