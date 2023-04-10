"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def postOrder(curr = root):
            nonlocal ans
            if curr:
                for i in curr.children:
                    postOrder(i)
                ans.append(curr.val)
        postOrder()
        return ans
        