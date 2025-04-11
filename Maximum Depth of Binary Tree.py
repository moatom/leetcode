# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        return l if l > r else r
    

'''
補助関数を使ったほうが速いのと、クロージャじゃなくて、グローバル変数使う
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def traverse(node, depth):
            nonlocal max_depth
            if not node:
                return
            
            max_depth = max(max_depth, depth)
            traverse(node.left, depth+1)
            traverse(node.right, depth+1)
        

        traverse(root, 1)
        return max_depth
'''