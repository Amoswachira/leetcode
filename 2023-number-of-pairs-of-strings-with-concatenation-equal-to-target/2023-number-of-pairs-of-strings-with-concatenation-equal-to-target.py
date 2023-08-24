class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
            prefix, suffix = Counter(), Counter()
            cnt = 0
            for num in nums:
                if target.startswith(num):
                    cnt += suffix[len(target) - len(num)]
                if target.endswith(num):
                    cnt += prefix[len(target) - len(num)]
                if target.startswith(num):
                    prefix[len(num)] += 1
                if target.endswith(num):
                    suffix[len(num)] += 1
            return cnt
        