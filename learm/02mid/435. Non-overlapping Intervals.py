# https://leetcode.com/problems/non-overlapping-intervals/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 終了時間でソート
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                # 重なっているので削除（カウントだけ進める）
                count += 1
            else:
                # 重なってないので更新
                prev_end = end

        return count

'''
つまり、 = 全区間数 - 最大の非重複区間数」

Greedyの戦略：
    終了時間が早い区間を優先的に選ぶ（保存区間に含む）と、後続の区間を入れられる余地が大きくなる。
    → 区間を end 昇順にソートし、重ならないものをカウント。
'''