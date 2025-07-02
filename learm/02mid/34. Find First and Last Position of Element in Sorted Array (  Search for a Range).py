# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def serach(isHigh):
            l = 0
            r = len(nums)-1

            bound = -1
            while l<=r:
                m = (l+r)//2
                if nums[m] < target: # exist in right
                    l = m+1
                elif nums[m] > target: # exist in left
                    r = m-1
                else:
                    bound = m
                    if isHigh:
                        l = m+1
                    else:
                        r = m-1
            return bound
        
        return [serach(False), serach(True)]
    
'''
right-exclusiveなのはなぜ？

'''