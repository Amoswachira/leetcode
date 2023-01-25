class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while j - i > 1:
            m = (i+j)//2
            if target <= nums[m]: j = m
            else: i = m
        return i if nums[i] == target else j if nums[j] == target else -1
        