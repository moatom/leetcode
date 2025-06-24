# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/?envType=problem-list-v2&envId=xo2bgr0r
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap): # このcapでdays以内のship可能かを検査
            d = 1
            total = 0
            for w in weights:
                if total+w>cap: # 総量がcapを超えるタイミングで別日へ
                    d += 1
                    total = 0
                total += w
            return d <= days # equal

        l,r = max(weights), sum(weights) # region
        while l<r:
            mid = (l+r)//2
            if canShip(mid): # ship可能な最小のcapを求めたい
                r = mid
            else:
                l = mid+1
        return l # l==rで修了
