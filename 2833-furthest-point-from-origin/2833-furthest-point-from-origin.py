class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a=moves.count('R')
        b=moves.count('L')
        c=moves.count('_')
        return abs(a-b)+c