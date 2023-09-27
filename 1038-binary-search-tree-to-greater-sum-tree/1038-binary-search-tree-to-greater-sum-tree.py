# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def reversedInorder(node: TreeNode, sm: int) -> int:
            if node:
                node.val += reversedInorder(node.right, sm)
                return reversedInorder(node.left, node.val)
            return sm

        reversedInorder(root, 0)
        return root