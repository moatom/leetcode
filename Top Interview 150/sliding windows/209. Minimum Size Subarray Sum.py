# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        min_len = len(nums)+1
        acc = 0
        while (j<len(nums)): # 追加対象の右端を動かすループから。
            acc += nums[j]
            while (acc >= target): # 最小化のロジックを実行するループ。
                min_len = min(min_len, j-i+1) # 一番いい点を探すべき。whileを一回も実行しないケースがある。
                acc -= nums[i]
                i += 1
            j += 1
        return min_len if min_len != len(nums)+1 else 0 # acc!=0だとうまくいかないケースがある。全部windowを捨てれば0になるので。
            
            