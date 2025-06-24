# https://leetcode.com/problems/longest-repeating-character-replacement/description/?envType=problem-list-v2&envId=oizxjoit

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # 変更が必要な数 > k の場合は左を縮める
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
