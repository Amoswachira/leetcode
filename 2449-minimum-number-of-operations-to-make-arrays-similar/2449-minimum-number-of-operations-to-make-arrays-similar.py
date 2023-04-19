class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        onums = sorted([x for x in nums if x % 2])
        enums = sorted([x for x in nums if x % 2 == 0])
        otar = sorted([x for x in target if x % 2])
        etar = sorted([x for x in target if x % 2 == 0])
        return sum((x - y) // 2 for x, y in zip(onums, otar) if x > y) + sum((x - y) // 2 for x, y in zip(enums, etar) if x > y)
        
        