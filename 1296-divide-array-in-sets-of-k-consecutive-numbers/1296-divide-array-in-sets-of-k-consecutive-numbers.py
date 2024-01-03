class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        while num_map:
            first = min(num_map)
            for i in range(first, first+k):
                if i not in num_map:
                    return False
                num_map[i] -= 1
                if num_map[i] == 0:
                    del num_map[i]
        return True