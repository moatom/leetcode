# https://leetcode.com/problems/validate-binary-search-tree/?envType=problem-list-v2&envId=xo2bgr0r
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(current, low, high):
            if not current:
                return True
            if not (low < current.val < high):
                return False

            return dfs(current.left, low, current.val) and \
                dfs(current.right, current.val, high)

        return dfs(root, float('-inf'), float('inf'))
