# https://leetcode.com/problems/minimum-depth-of-binary-tree/?envType=problem-list-v2&envId=xo2bgr0r

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # XXX
            return 0

        q = deque([root])
        level = 1

        while q:
            for _ in range(len(q)): # bfs by level
                current = q.popleft()
                if not current: # None case
                    continue
                if not current.left and not current.right:
                    return level

                q.append(current.left)
                q.append(current.right)
            level += 1

'''
講評：
rootが空の場合の例外ケース、dequeがcollections由来であること。変数名がdepth

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

レベル単位の処理がいらないので、こういうbfsも可能。（queue内でdepthをトレースできないと駄目だけど。）
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])  # (node, depth)

        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
'''

'''
逆に、レベル別処理のパターン：
例1: 二分木のレベルごとのノード一覧を作る（レベル別にまとめる）
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        size = len(queue)
        level_nodes = []  # 今のレベルのノードをためる
        for _ in range(size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_nodes)  # レベル単位でまとめて追加
    return result

例2: 最短距離が特定のレベルに達したら途中で探索をやめる
def bfs_early_stop(graph, start, max_level):
    visited = set([start])
    queue = deque([start])
    level = 0

    while queue:
        if level > max_level:
            break  # max_level超えたら探索終了
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            # nodeの処理
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1

例3: レベルごとに集計や判定をしたいケース
例えば、迷路探索で「何手目でどこまで行けるか」を調べたいとき。
def bfs_steps(graph, start):
    visited = set([start])
    queue = deque([start])
    steps = 0

    while queue:
        size = len(queue)
        print(f"Step {steps}: {size} nodes reachable")
        for _ in range(size):
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        steps += 1
'''