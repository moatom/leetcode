# https://leetcode.com/problems/insert-interval/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i<n:
            res.append(intervals[i])
            i += 1
        
        return res

'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1. newInterval の前にあるものを追加
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. 重なっている区間をマージ
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. 残りを全部追加
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
'''