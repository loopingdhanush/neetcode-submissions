# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        temp = []
        temp.append(root)

        while temp:
            qlevel = len(temp)
            level = []
            for i in range(qlevel):
                node = temp.pop(0)
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if level:
                res.append(level)
        return res