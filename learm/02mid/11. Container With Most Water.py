class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # 低い方を動かす
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

'''
sliding windowではないので、両側の操作がありうる。
'''