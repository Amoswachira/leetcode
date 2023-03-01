class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        twoBack = 0
        oneBack = nums[0]
        for n in range(1,len(nums)):
            temp = oneBack
            # Choice between include current house in robbing or not
            oneBack = max(oneBack, nums[n] + twoBack)
            twoBack = temp

        return oneBack
        