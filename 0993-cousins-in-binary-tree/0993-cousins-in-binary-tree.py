class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q=deque([(root,0)])
        result=[]
        h={}
        while q:
            level=[]
            for i in range(len(q)):
                a,fat=q.popleft()
                level.append(a.val)
                h[a.val]=fat
                if a.left:
                    q.append((a.left,a.val))
                if a.right:
                    q.append((a.right,a.val))
            result.append(level)
        if h[x]==h[y]:
            return False
        for i in range(len(result)):
            if x in result[i] and y in result[i]:
                return True
        return False
        