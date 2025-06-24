# https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=xo2bgr0r
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)

        for i in range(1, len(s)+1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[-1]

'''
🔍 補足
    s[j:i] が辞書にあり、dp[j] == True なら dp[i] = True
    内側の for j in range(i) は、すべての区切り方をチェックしている

from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @lru_cache(None)
        def dfs(start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and dfs(end): # 各startに対し、全てのendの区切りパターンを試す
                    return True
            return False

        return dfs(0)
'''
