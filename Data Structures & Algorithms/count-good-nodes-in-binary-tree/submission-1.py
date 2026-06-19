# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if not node:
                return 0
            good = 1 if node.val >= curr_max else 0
            curr_max = max(node.val, curr_max)

            return (good+dfs(node.left,curr_max)+dfs(node.right, curr_max))

        return dfs(root, root.val)
        