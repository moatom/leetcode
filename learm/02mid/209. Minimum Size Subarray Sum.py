# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=xo2bgr0r
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_size = float('inf') # 初期値はでかい値。未達の場合はこのまま可笑しいので、そこの処理が必要。

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_size = min(right-left+1, min_size)
                # right分を取り消した時点で、必ずtarget>=1よりは小さくなるので、left<=rightは保証
                total -= nums[left]
                left += 1

        return 0 if min_size == float('inf') else min_size

'''
駄目な例：
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        min_size = float('inf') # 初期値はでかい値

        while right<len(nums):
            total += nums[right] # これだと、rightを進めていない場合もtotalに加算されてしまう。2 pointerやsliding windowは、for loop軸のほうが考えやすい。
            if total >= target:
                print(total)
                min_size = min(right-left+1, min_size)
                if left<right:
                    total -= nums[left]
                    left += 1
                elif left==right:
                    return 1
            else:
                right += 1

        return min_size
'''