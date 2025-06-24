# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=problem-list-v2&envId=xo2bgr0r

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.__k = k
        self.__nums = nums
        heapq.heapify(self.__nums)
        while len(self.__nums) > k:
            heapq.heappop(self.__nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.__nums, val)
        while len(self.__nums) > self.__k:
            heapq.heappop(self.__nums)
        return self.__nums[0]
