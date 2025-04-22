# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rst = list()
        q = list()
        if root:
            q.append(root)
        else:
            return []
        while q:
            rst.append([_.val for _ in q])
            fl_size = len(q)
            for i in range(fl_size):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]
        
        return rst

        
        
