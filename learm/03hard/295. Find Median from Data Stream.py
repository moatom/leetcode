# https://leetcode.com/problems/find-median-from-data-stream/description/?envType=problem-list-v2&envId=oizxjoit

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (Pythonはmin heapなので値を反転させて管理)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # small にまず入れる（max heapにするため -num）
        heapq.heappush(self.small, -num)

        # smallの最大値が large の最小値より大きければ入れ替え
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # サイズ調整
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

'''
キモ：
中央値は「データを小さい順に並べたとき中央の値」
よく使う手法：

2つのヒープを使う（最大ヒープと最小ヒープ）
    最大ヒープ: 小さいほうの半分の値を管理（中で最大の値がトップ）
    最小ヒープ: 大きいほうの半分の値を管理（中で最小の値がトップ）

動作イメージ
    新しい値が入ったら、どちらかのヒープに入れる。
    両方のヒープのサイズ差が1以上にならないように調整する。
    ヒープのサイズが同じなら中央値は両ヒープトップの平均。
    サイズが違うなら、大きい方のヒープのトップが中央値。
'''