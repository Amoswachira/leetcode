class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        def findRoot() -> int:
            seen = set(range(n))
            seen.difference_update(leftChild + rightChild)
            return seen.pop() if len(seen) == 1 else -1
        
        def bfs(root: int) -> bool:
            dq, seen = deque([root]), {root}
            while dq:
                node = dq.popleft()
                for kid in leftChild[node], rightChild[node]:
                    if kid >= 0:
                        if kid in seen:
                            return False
                        seen.add(kid)
                        dq.append(kid)
            return len(seen) == n
    
        root = findRoot()
        return root >= 0 and bfs(root)
        