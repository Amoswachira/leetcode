class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_set = set()

        for num in nums:
            if num in unique_set:
                unique_set.remove(num)
            else:
                unique_set.add(num)

        return unique_set.pop()