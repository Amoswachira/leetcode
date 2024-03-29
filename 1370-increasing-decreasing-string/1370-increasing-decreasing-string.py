class Solution:
    def sortString(self, s: str) -> str:
        counter, result = collections.Counter(s), []
        while counter:
            for traverse in string.ascii_lowercase, reversed(string.ascii_lowercase):
                result += [c for c in traverse if c in counter]
                counter -= dict.fromkeys(counter, 1)
        return ''.join(result)
        