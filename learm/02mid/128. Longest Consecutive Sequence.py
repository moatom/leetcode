# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # 先にset化で参照
        max_len = 0

        for num in num_set:
            # 連続列の始点のみ処理
            if num - 1 not in num_set:
                current = num # 始点の初期化
                length = 1

                while current + 1 in num_set: # ある限り成長
                    current += 1
                    length += 1

                max_len = max(max_len, length) # 更新

        return max_len
'''
num - 1 not in num_set で、始点かどうかを高速にチェック。
set にすることで、存在確認が O(1) になり、全体で O(n) を達成。
ソートを使わずに済む。
'''
