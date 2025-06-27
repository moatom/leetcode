# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        max_area = 0
        while l<r:
            area = min(height[l], height[r]) * (r-l)
            max_area =  max(area, max_area)

            if height[l] > height[r]:
                r-=1
            else:
                l+=1

        return max_area
    
'''
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

sliding windowではないので、両側の操作がありうる。
'''