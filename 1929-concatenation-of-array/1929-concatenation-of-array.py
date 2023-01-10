class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        the_stack = deque()
        
        for j in range(len(nums)):
            the_stack.append(nums[j])
        
        for i in range(len(nums)):
            the_stack.append(nums[i])
        
        
        return the_stack