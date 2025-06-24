# https://leetcode.com/problems/subarray-sum-equals-k/description/?envType=problem-list-v2&envId=xo2bgr0r
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # 重要：最初に合計が0のprefixが1つあるとみなす
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num # [0..j]
            count += prefix_count[curr_sum - k]  # ここが核心：k=[i+1..j]を満たす累積和[0..i]のi(i<j = i+1<=j)の、いままでの出現回数を求める
            prefix_count[curr_sum] += 1

        return count


'''
-1000 <= nums[i] <= 1000
-107 <= k <= 107
---
    sum[0..j] - sum[0..i] == k なら、区間 [i+1..j] の合計が k
    このとき sum[0..i] = sum[0..j] - k を満たす i を探せばよい！
---
O(n^2) = O(4*10^8) > 10^7 * 0.1 us = 1 s
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.count = 0

        def backtrack(start, total):
            if total == k:
                self.count += 1
            if start >= n:
                return
            backtrack(start + 1, total + nums[start])

        for i in range(n):
            backtrack(i, 0)
        return self.count
'''
