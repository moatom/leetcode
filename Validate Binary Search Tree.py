# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def max_dfs(root, val):
            if not root:
                return True
            
            if root.val >= val:
                return False
            
            return max_dfs(root.left, val) and max_dfs(root.right, val)
        
        def min_dfs(root, val):
            if not root:
                return True
            
            if root.val <= val:
                return False
            
            return min_dfs(root.left, val) and min_dfs(root.right, val)
        
        return max_dfs(root.left, root.val) and \
               min_dfs(root.right, root.val) and \
               self.isValidBST(root.left) and \
               self.isValidBST(root.right)

'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        prev = None

        for val in inorder(root):
            if prev is None or prev < val:
                prev = val
            else:
                return False

        return True
ーーー
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        
        return isValid(root, float('-inf'), float('inf'))
'''
