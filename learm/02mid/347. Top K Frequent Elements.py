# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        num_freq_map = Counter(nums)
        
        for (num, freq) in num_freq_map.items():
            # 最小ヒープは小さい方から捨てられる。　頻度の小さい順に並べ、小さい方から不要になったら捨てていく。
            # 最終的に大きい方からk個まで残しておけばいい。
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return list(map(lambda x: x[1], heap))
