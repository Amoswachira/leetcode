class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
    
        for x in nums:
            if x in hash_set:
                return True
            hash_set.add(x)
        return False
        