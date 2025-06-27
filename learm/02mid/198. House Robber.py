class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-2]+nums[i] xor dp[i-1]でdp[i-2]より大きいやつになった場合)
        #       = max(dp[i-2]+nums[i] or dp[i-1])
        #  where dp[0] = nums[0]
        n = len(nums)
        if n == 1:  # XXX
            return nums[0]


        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        # i>2を仮定しているので、例外処理が必要。先にテンプレで雑に処理すると忘れやすいので、確実に処理すべき。

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]) # nums[i]が重要.また、curr, prevに最適化可能: prev, curr = curr, max(curr, prev+nums[i])

        return dp[n-1]