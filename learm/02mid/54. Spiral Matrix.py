# https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            # → 右
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # ↓ 下
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # ← 左
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # ↑ 上
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
