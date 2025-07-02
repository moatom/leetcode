# https://leetcode.com/problems/sort-colors/description/

#  Dutch National Flag アルゴリズム
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        current=0
        
        while current<=r:
            if nums[current] == 0:
                nums[l], nums[current] = nums[current], nums[l]
                l+=1 # ないと、[0,1,0]でバグる
                current+=1
            elif nums[current] == 1:
                current+=1
            elif nums[current] == 2:
                nums[current], nums[r] = nums[r], nums[current]
                r-= 1

'''
nums[current] == 0:
で
l+=1
すると、2とswapされた場合の検査ができない気がする？
↑nums[l..current-1] == 1で1を一時保存しておくので、そこを潰しては行けない。負にはならない。

保証されている不変条件：
nums[0..l-1] == 0
nums[l..current-1] == 1
nums[current..r] == 未検査
nums[r+1..] == 2

nums[current..r] == 未検査
を潰すまでのループなので、ここに1要素でもあってはいけない。
'''


# カウントソート
def sortColors(nums):
    count = [0, 0, 0]

    # カウント（1パス目）
    for num in nums:
        count[num] += 1

    # 上書き（2パス目）
    index = 0
    for i in range(3):
        for _ in range(count[i]):
            nums[index] = i
            index += 1
