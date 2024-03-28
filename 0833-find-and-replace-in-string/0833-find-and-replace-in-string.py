class Solution:
    def findReplaceString(self, S, indices, sources, targets):
            """
            :type S: str
            :type indexes: List[int]
            :type sources: List[str]
            :type targets: List[str]
            :rtype: str
            """

            modified = list(S)
            for index, source, target in zip(indices, sources, targets):
                if not S[index:].startswith(source):
                    continue
                else:
                    modified[index] = target
                    for i in range(index+1, len(source) + index):
                        modified[i] = ""

            return "".join(modified)
        