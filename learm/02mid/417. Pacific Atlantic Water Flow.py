# https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited, prev_height):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                (i, j) in visited or
                heights[i][j] < prev_height # 海側から見て、heightは非減少列でないと駄目
            ):
                return
            visited.add((i, j))
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i + dx, j + dy, visited, heights[i][j])

        # 上下の端（Pacific: 上 / Atlantic: 下）
        for col in range(n):
            dfs(0, col, pacific, heights[0][col])        # 上
            dfs(m - 1, col, atlantic, heights[m - 1][col]) # 下

        # 左右の端（Pacific: 左 / Atlantic: 右）
        for row in range(m):
            dfs(row, 0, pacific, heights[row][0])        # 左
            dfs(row, n - 1, atlantic, heights[row][n - 1]) # 右

        # 両方に到達可能なマスを集める
        return list(pacific & atlantic)
