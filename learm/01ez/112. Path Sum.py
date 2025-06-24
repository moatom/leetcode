# https://leetcode.com/problems/path-sum/description/?envType=problem-list-v2&envId=xo2bgr0r

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            if not node.left and not node.right:
                return current_sum + node.val == targetSum

            return dfs(node.left, current_sum + node.val) or \
                dfs(node.right, current_sum + node.val)

        if not root:
            return False
        return dfs(root, 0)

'''
講評：
leafの判定と、空nodeの例外処理がむずい


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        # If it's a leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        # Subtract current node value from targetSum and recurse
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )

'''