def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(nums):
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr

    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

'''
✅ 解法：DP + 2回試す
🧠 ポイント
    通常の House Robber I（直線） では、dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    今回は環状なので、「最初の家を選ぶと、最後の家は選べない」という制約がある

🔁 だから、次の2通りで比較する：
    家0を除く範囲：nums[1:]
    家n-1を除く範囲：nums[:-1]
'''