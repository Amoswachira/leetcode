class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}
        
        for i , num in enumerate(nums):
            compliment = target - num
            
            if compliment in num_indices:
                return [num_indices[compliment] , i]
            num_indices[num] = i
        return []
        